from math import remainder
from multiprocessing.connection import Client
from pickle import FALSE
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from seller import models as am
from .models import *
import email
import re
from django.shortcuts import redirect, render
from . models import *
from random import choices, randrange
from django.conf import settings
from django.core.mail import send_mail
from datetime import date

import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest

# Create your views here.

def client_index(request):
    services = am.Service.objects.all()
    try:
        uid = ClientUser.objects.get(email=request.session['client'])
        return render(request,'client-index.html',{'uid':uid,'services':services})    
    except:
        return render(request,'client-index.html',{'services':services})

def client_view_service(request,pk):
    service = am.Service.objects.get(id=pk)
    try:
        uid = ClientUser.objects.get(email=request.session['client'])
        return render(request,'client-view-service.html',{"uid":uid,'service':service})
    except:
        return render(request,'client-view-service.html',{'service':service})

def client_signin(request):
    # services = am.Service.objects.all()
    if request.method == 'POST':
        try:
            uid = ClientUser.objects.get(email=request.POST['email'])
            if request.POST['password'] == uid.password:
                request.session['client'] = request.POST['email']
                return redirect('client_index')
            return render(request,'client-signin.html',{'msg':'Pasword is incorrect'})
        except:
            return render(request,'client-signin.html',{'msg':'Acccount does not exists'})
    return render(request,'client-signin.html')
    

def client_signup(request):
    if request.method == "POST":
        try:
            ClientUser.objects.get(email=request.POST['email'])
            msg = 'Email already exist'
            return render(request,'client-signup.html',{'msg':msg})
        except:
            if request.POST['password'] == request.POST['cpassword']:
                otp = randrange(1000,9999)
                subject = 'OTP verification'
                message = f'''Hi User,
                Welcome to E-Civil,
                We to thankful to you for joining with us...
                Your OTP is {otp}'''
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST['email'], ]
                send_mail( subject, message, email_from, recipient_list )
                global temp
                temp = {
                    'fname' : request.POST['fname'],
                    'lname' : request.POST['lname'],
                    'email' : request.POST['email'],
                    'mobile' : request.POST['mobile'],
                    'password' : request.POST['password'],
                }
                return render(request,'client-otp.html',{'msg':'OTP sent on your Email!!','otp':otp})
            return render(request,'client-signup.html',{'msg':'Both are not same'})
    return render(request,'client-signup.html')

def client_otp(request):
    if request.POST['uotp'] == request.POST['otp']:
        global temp
        ClientUser.objects.create(
            fname = temp['fname'],
            lname = temp['lname'],
            email = temp['email'],
            mobile = temp['mobile'],
            password = temp['password'],
        )
        del temp
        return render(request,'client-signin.html',{'msg':'Account Created'})
    return render(request,'client-otp.html',{'msg':'Invalid OTP','otp':request.POST['otp']})

def client_logout(request):
    # services = am.Service.objects.all()
    del request.session['client']
    return redirect('client_index')

def client_forgot(request):
    if request.method == 'POST':
        try:
            uid = ClientUser.objects.get(email=request.POST['email'])
            s = '1234567890qwertyuiopasdfghjklzxcvbnm@'
            password = ''.join(choices(s,k=8))
            subject = 'Reset Password'
            message = f'''Hi User,
            Your New password is : {password}'''
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST['email'], ]
            send_mail( subject, message, email_from, recipient_list )
            uid.password = password
            uid.save()
            return render(request,'client-signin.html',{'msg':'Password sent on your mail....'})

        except:
            return render(request,'client-forgot.html',{'msg':'Account does not exist!!'})
    return render(request,'client-forgot.html')

def client_profile(request):
    uid = ClientUser.objects.get(email=request.session['client'])
    if request.method == 'POST':
        
        uid.fname = request.POST['fname']
        uid.lname = request.POST['lname']
        uid.mobile = request.POST['mobile']
        uid.address = request.POST['address']
        uid.country = request.POST['country']
        uid.state = request.POST['state']
        uid.district = request.POST['district']
        uid.pincode = request.POST['pincode']
        
        if 'pic' in request.FILES:
            uid.pic = request.FILES['pic']
            
        uid.save()
        return render(request, 'client-profile.html',{'uid':uid,'msg':'Profile has been updated'})
    return render(request, 'client-profile.html',{'uid':uid})
def book_prod(request,pk):
    uid = ClientUser.objects.get(email=request.session['client'])
    # try:
    client = ClientUser.objects.get(email=request.session['client'])
    if request.method == 'POST':
        service = Service.objects.get(id=pk)
        book = Booking.objects.create(
            service = service,
            book_date = date.today(),
            address = request.POST['address'],
            quantity = request.POST['quantity'],
            client = client,
            amount = int(request.POST['quantity'])*int(service.price),
        )
        currency = 'INR'
        amount = int(book.quantity)*int(service.price)*100  # Rs. 200
    
        # Create a Razorpay Order
        razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                        currency=currency,
                                                        payment_capture='0'))
    
        # order id of newly created order.
        razorpay_order_id = razorpay_order['id']
        callback_url = f'paymenthandler/{book.id}'
    
        # we need to pass these details to frontend.
        context = {}
        context['razorpay_order_id'] = razorpay_order_id
        context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
        context['razorpay_amount'] = amount
        context['currency'] = currency
        context['callback_url'] = callback_url
        context['book'] = book
        context['uid']= uid
        context['date']= date.today()
        
        return render(request,'book_proceed.html',context=context)
    return render(request,'book-prod.html',{'uid':uid})
    # except:
        # return redirect('client_signin')

# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

 
# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request,pk):
    uid = ClientUser.objects.get(email=request.session['client'])
    # only accept POST request.
    if request.method == "POST":
        try:
            book = Booking.objects.get(id=pk)
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            # if result is None:
            # amount = int(book.amount)*100  # Rs. 200
            amount = int(book.amount)*100  # Rs. 200

            try:

                # capture the payemt
                razorpay_client.payment.capture(payment_id, amount)

                book.pay_id = payment_id
                book.verify = True
                book.save()

                # render success page on successful caputre of payment
                return render(request, 'book-prod.html',{'uid':uid,'msg':'Order Placed Successfully...'})
            except:

                # if there is an error while capturing payment.
                return render(request, 'book-prod.html',{'uid':uid,'msg':'Payment failed !!! Try Again...'})
            # else:
 
            #     # if signature verification fails.
            #     return render(request, 'paymentfail.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()


def view_order(request):
    uid = ClientUser.objects.get(email=request.session['client'])
    booking = Booking.objects.filter(
        client = uid,
        verify = True,
    )[::-1]
    return render(request,'view_order.html',{'uid':uid,'booking':booking})

def order_detail(request,pk):
    uid = ClientUser.objects.get(email=request.session['client'])
    book = Booking.objects.get(id = pk)
    return render(request,'order_detail.html',{'uid':uid,'book':book})

def order_status(request,pk):
    uid = ClientUser.objects.get(email=request.session['client'])
    book = Booking.objects.get(id = pk)
    return render(request,'order_status.html',{'uid':uid,'book':book})

def client_contact(request):
    try:
        uid = ClientUser.objects.get(email=request.session['client'])
        return render(request,'client-contact.html',{'uid':uid})    
    except:
        return render(request,'client-contact.html')


def client_service(request):
    try:
        uid = ClientUser.objects.get(email=request.session['client'])
        return render(request,'client-service.html',{'uid':uid})    
    except:
        return render(request,'client-service.html')


def client_about(request):
    try:
        uid = ClientUser.objects.get(email=request.session['client'])
        return render(request,'client-about.html',{'uid':uid})    
    except:
        return render(request,'client-about.html')
