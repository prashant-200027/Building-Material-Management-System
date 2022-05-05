from http import client
from django.shortcuts import render, redirect
from .models import * 
from random import randrange, choices
from client.models import *
# mail 
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def index(request):
    try:
        uid = User.objects.get(email=request.session['email'])
        orders = Booking.objects.filter(service__provider = uid,verify=True)
        count = 0
        for i in orders:
            count = count+1
        
        services = Service.objects.filter(provider=uid)
        scount = 0
        for j in services:
            scount = scount+1
        
        bookings = Booking.objects.filter(service__provider = uid,verify=True)[:5:-1]

        return render(request,'index.html',{'uid':uid,'count':count,'scount':scount,'bookings':bookings})
    except:
        return render(request,'signin.html',{'msg':'Session has expired'})

def signup(request):
    if request.method == "POST":
        try:
            User.objects.get(email=request.POST['email'])
            msg = 'Email already exist'
            return render(request,'signup.html',{'msg':msg})
        except:
            if request.POST['password'] == request.POST['cpassword']:
                otp = randrange(1000,9999)
                subject = 'OTP verification'
                message = f'''Hello User!!!
                Welcome to E-Civil,
                We to thankful to you for joining with us...
                Thank You for the sharing your products with..
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
                return render(request,'otp.html',{'msg':'OTP sent on your Email!!','otp':otp})
            return render(request,'signup.html',{'msge':'Both are not same'})
    return render(request,'signup.html')

def otp(request):
    if request.POST['uotp'] == request.POST['otp']:
        global temp
        User.objects.create(
            fname = temp['fname'],
            lname = temp['lname'],
            email = temp['email'],
            mobile = temp['mobile'],
            password = temp['password'],
        )
        del temp
        return render(request,'signin.html',{'msg':'Account Created'})
    return render(request,'otp.html',{'msge':'Invalid OTP','otp':request.POST['otp']})


def signin(request):
    if request.method == 'POST':
        try:
            uid = User.objects.get(email=request.POST['email'])
            if request.POST['password'] == uid.password:
                request.session['email'] = request.POST['email']
                return redirect('index')
            return render(request,'signin.html',{'msg':'Pasword is incorrect'})
        except:
            return render(request,'signin.html',{'msg':'Acccount does not exists'})
    return render(request,'signin.html')

def logout(request):
    del request.session['email']
    return redirect('signin')

def forgot(request):
    if request.method == 'POST':
        try:
            uid = User.objects.get(email=request.POST['email'])
            s = 'qweertyuiopasdfghklxcvbnm12345684556$%$#'
            password = ''.join(choices(s,k=8))  
            subject = 'Password Has Been Reset'
            message = f'''Your New password is {password}'''
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST['email'], ]
            send_mail( subject, message, email_from, recipient_list )
            uid.password = password
            uid.save()
            return render(request,'signin.html',{'msg':'Ne wpassword sent on your email'})

        except:
            return render(request,'forgot.html',{'msg':'Account does not exist'})
    return render(request,'forgot.html')

def changepswd(request):
    uid = User.objects.get(email=request.session['email'])

    if request.method == "POST":
            uid = User.objects.get(email=request.session['email'])
            if request.POST['cpswd'] == uid.password:
                if request.POST['npswd'] == request.POST['cnpswd']:
                    uid.password = request.POST['npswd']
                    uid.save()
                    return render(request,'index.html',{'uid':uid,'msg': 'Password change Successfully...'})
                return render(request,'changepswd.html',{'uid':uid,'msg': 'Both New password are not same...'})
            return render(request, 'changepswd.html',{'uid':uid,'msg':'current password is invalid!!!'})
    return render(request, 'changepswd.html',{'uid':uid})

def profile(request):
    uid = User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        
        uid.fname = request.POST['fname']
        uid.lname = request.POST['lname']
        uid.mobile = request.POST['mobile']
        uid.address = request.POST['address']
        uid.country = request.POST['country']
        uid.state = request.POST['state']
        uid.district = request.POST['district']
        uid.pincode = request.POST['pincode']
        uid.aadhar = request.POST['aadhar']
        
        if 'pic' in request.FILES:
            uid.pic = request.FILES['pic']
        if 'aadharpic' in request.FILES:
            uid.aadharpic = request.FILES['aadharpic']
            
        uid.save()
        return render(request, 'profile.html',{'uid':uid,'msg':'Profile has been updated'})
    return render(request, 'profile.html',{'uid':uid})

def service(request):
    uid = User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        Service.objects.create(
            provider = uid,
            shopname = request.POST['shopname'],
            typematerial = request.POST['typematerial'],
            country = request.POST['country'],
            state = request.POST['state'],
            district = request.POST['district'],
            pincode = request.POST['pincode'],
            mname = request.POST['mname'],
            mimage = request.FILES['mimage'],
            price = request.POST['price'],
            weights = request.POST['weights'],
            nomc = request.POST['nomc'],
            proddesc = request.POST['proddesc'],
        )
        msg = 'Material added Successfully'
        return render(request,'service.html',{'uid':uid, 'msg':msg})
    return render(request,'service.html',{'uid':uid})

def myservice(request):
    uid = User.objects.get(email=request.session['email'])
    services = Service.objects.filter(provider=uid)
    return render(request,'myservice.html',{'uid':uid,'services':services})

def delete_service(request,pk):
    uid = User.objects.get(email=request.session['email'])
    service = Service.objects.get(id=pk)
    service.delete()
    return redirect('myservice')

def inactive_service(request,pk):
    uid = User.objects.get(email=request.session['email'])
    service = Service.objects.get(id=pk)
    service.acitive = False
    service.save()
    return redirect('myservice')

def active_service(request,pk):
    uid = User.objects.get(email=request.session['email'])
    service = Service.objects.get(id=pk)
    service.acitive = True
    service.save()
    return redirect('myservice')

def edit_service(request,pk):
    uid = User.objects.get(email=request.session['email'])
    service = Service.objects.get(id=pk)
    if request.method == 'POST':
        # service.name = request.POST['sname']
        # service.sector = request.POST['sector']
        # service.min_charge= request.POST['charge']
        # service.area = request.POST['area']
        # service.desc = request.POST['desc']

        # print(request.POST['weights'],type(request.POST['weights']))
        service.shopname = request.POST['shopname']
        service.typematerial = request.POST['typematerial']
        service.country = request.POST['country']
        service.state = request.POST['state']
        service.district = request.POST['district']
        service.pincode = request.POST['pincode']
        service.mname = request.POST['mname']
        service.price = request.POST['price']
        service.weights = int(request.POST['weights'])
        service.nomc = request.POST['nomc']
        service.proddesc = request.POST['proddesc']
        # service.acitive = request.POST['acitive']
        service.save()
        return redirect('myservice')
    return render(request,'edit-service.html',{'uid': uid,'service':service})

def view_client_booking(request):
    uid = User.objects.get(email=request.session['email'])
    
    bookings = Booking.objects.filter(service__provider = uid,verify=True)

    return render(request,'view-client-booking.html',{'uid':uid,'bookings':bookings})  #,'bookings':bookings

def view_client_book(request,pk):
    uid = User.objects.get(email=request.session['email'])
    booking = Booking.objects.get(id=pk)
    return render(request,'view-client-book.html',{'uid':uid,'booking':booking})


def order_dispetch(request,pk):
    book = Booking.objects.get(id=pk)
    book.status = True
    book.action = True
    book.save()
    return redirect('view-client-booking')

def order_ofd(request,pk):
    book = Booking.objects.get(id=pk)
    book.sta = True
    book.act = True
    book.save()
    return redirect('view-client-booking')

def order_dvd(request,pk):
    book = Booking.objects.get(id=pk)
    book.st = True
    book.ac = True
    book.save()
    return redirect('view-client-booking')
