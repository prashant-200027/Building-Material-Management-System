from concurrent.futures.process import _ThreadWakeup
from http import client
from tokenize import blank_re
from django.db import models

# Create your models here.
from audioop import maxpp
import email
from operator import truediv
from pyexpat import model
from django.db import models

from bmms.models import *

# Create your models here.
# ORM : OBJECT RELATIONAL MAPPING

# database table creation 

class Client(models.Model):

    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    pic = models.FileField(upload_to='Clientprofile',default='avtar.png')
    address = models.TextField(null=True,blank=True)
    country = models.CharField(max_length=10,blank=True,null=True)
    state = models.CharField(max_length=10,blank=True,null=True)
    district = models.CharField(max_length=20,blank=True,null=True)
    pincode = models.CharField(max_length=20,blank=True,null=True)

    # perticular attribute function 
    def __str__(self):
        return self.fname + ' ' + self.lname

class Booking(models.Model):
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    book_date = models.DateField(null=True,blank=True)
    amount = models.IntegerField(default=0)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    address = models.TextField(null=True,blank=True)
    pay_id = models.CharField(max_length=30,null=True,blank=True)
    verify = models.BooleanField(default=False)
    pay_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.service.mname    