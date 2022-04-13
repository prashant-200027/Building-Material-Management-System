import email
import re
from django.shortcuts import redirect, render
from . models import *
from random import choices, randrange
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.

from django.shortcuts import render

from bmms.models import User

# Create your views here.

def index(request):
    try:
        uid = User.objects.get(email=request.session['email'])
        return render(request,'index.html',{'uid':uid})
    except:
        return render(request,'sign-in.html',{'msg':'Session has expired'})

def signin(request):
    if request.method == 'POST':
        try:
            uid = User.objects.get(email=request.POST['email'])
            if request.POST['password'] == uid.password:
                request.session['email'] = request.POST['email']
                # return redirect('index')
                return render(request,'index.html',{'uid':uid})
            return render(request,'sign-in.html',{'msg':'Pasword is incorrect'})
        except:
            return render(request,'sign-in.html',{'msg':'Acccount does not exists'})
    return render(request,'sign-in.html')

def signup(request):
    if request.method == "POST":
        try:
            User.objects.get(email=request.POST['email'])
            msg = 'Email already exist'
            return render(request,'sign-up.html',{'msg':msg})
        except:
            if request.POST['password'] == request.POST['cpassword']:
                otp = randrange(1000,9999)
                subject = 'OTP verification'
                message = f'Your OTP is {otp}'
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
            return render(request,'sign-up.html',{'msg':'Both are not same'})
    return render(request,'sign-up.html')

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
        return render(request,'sign-in.html',{'msg':'Account Created'})
    return render(request,'otp.html',{'msg':'Invalid OTP','otp':request.POST['otp']})

def logout(request):
    del request.session['email']
    return render(request,'sign-in.html')

def forgot(request):
    if request.method == 'POST':
        try:
            uid = User.objects.get(email=request.POST['email'])
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
            return render(request,'sign-in',{'msg':'Password sent on your mail....'})

        except:
            return render(request,'forgot.html',{'msg':'Account does not exist!!'})
    return render(request,'forgot.html')

def changepswd(request):
    if request.method == "POST":
            uid = User.objects.get(email=request.session['email'])
            if request.POST['cpswd'] == uid.password:
                if request.POST['npswd'] == request.POST['cnpswd']:
                    uid.password = request.POST['npswd']
                    uid.save()
                    return render(request,'index.html',{'msg': 'password is changed...'})
                return render(request,'changepswd.html',{'msg': 'Both New password are not same...'})
            return render(request, 'changepswd.html',{'msg':'current password is invelid!!!'})
    return render(request, 'changepswd.html')


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
            # acitive = request.POST['acitive'],
        )
        msg = 'Service added Successfully'
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
        service.name = request.POST['sname']
        service.sector = request.POST['sector']
        service.min_charge= request.POST['charge']
        service.area = request.POST['area']
        service.desc = request.POST['desc']
        service.save()
        return redirect('myservice')
    return render(request,'edit-service.html',{'uid': uid,'service':service})
