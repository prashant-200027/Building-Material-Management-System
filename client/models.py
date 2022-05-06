from django.db import models

from seller.models import *
# Create your models here.

class ClientUser(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    address = models.TextField()
    pic = models.FileField(upload_to='Clientprofile',default='avtar.png')
    country = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    district = models.CharField(max_length=20)
    pincode = models.CharField(max_length=20)

    def __str__(self):
        return self.fname + ' ' + self.lname

class Booking(models.Model):
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    client = models.ForeignKey(ClientUser,on_delete=models.CASCADE)
    book_date = models.DateField(null=True,blank=True)
    amount = models.IntegerField(default=0)
    pay_id = models.CharField(max_length=30,null=True,blank=True)
    verify = models.BooleanField(default=False)
    pay_at = models.DateTimeField(auto_now_add = True)
    quantity = models.IntegerField(default=0)
    address = models.TextField(null=True,blank=True)
    status = models.BooleanField(default=False)
    action = models.BooleanField(default=False)
    sta = models.BooleanField(default=False)
    act = models.BooleanField(default=False)
    st = models.BooleanField(default=False)
    ac = models.BooleanField(default=False)

    def __str__(self):
        return self.service.mname    

class Contact(models.Model):
    name = models.CharField(max_length=30,null=True,blank=True)
    email = models.CharField(max_length=30,null=True,blank=True)
    subject = models.CharField(max_length=30,null=True,blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name 