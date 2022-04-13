from audioop import maxpp
import email
from operator import truediv
from os import stat
from pyexpat import model
from django.db import models

# Create your models here.
# ORM : OBJECT RELATIONAL MAPPING

# database table creation 

class User(models.Model):

    cou = [('India','India')]
    sta = [('Gujarat','Gujarat'),('Goa','Goa'),('Delhi','Delhi'),('Rajasthan','Rajasthan'),]
    

    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    address = models.TextField(null=True,blank=True)
    country = models.CharField(max_length=10,blank=True,null=True)
    state = models.CharField(max_length=10,blank=True,null=True)
    district = models.CharField(max_length=20,blank=True,null=True)
    pincode = models.CharField(max_length=20,blank=True,null=True)
    aadhar = models.CharField(max_length=15,blank=True,null=True)
    aadharpic = models.FileField(upload_to='AadharPic',blank=True,null=True)
    pic = models.FileField(upload_to='profile',default='avtar.png')

    # perticular attribute function 
    def __str__(self):
        return self.fname + ' ' + self.lname

class Service(models.Model):

    mat = [('Cement','Cement'),('Plumbing','Plumbing'),('Painting','Painting'),('Furniture','Furniture'),('TextTile','TextTile')]
    cntry = [('India','India')]
    stat = [('Gujarat','Gujarat'),('Goa','Goa'),('Delhi','Delhi'),('Rajsthan','Rajsthan')]


    provider = models.ForeignKey(User,on_delete=models.CASCADE)
    shopname = models.CharField(max_length=100)
    typematerial = models.CharField(max_length=100, choices=mat)
    country = models.CharField(max_length=10,null=True,blank=True,choices=cntry)
    state = models.CharField(max_length=10,null=True,blank=True,choices=stat)
    district = models.CharField(max_length=100,null=True,blank=True)
    pincode = models.CharField(max_length=100,null=True,blank=True)
    mname = models.CharField(max_length=100,null=True,blank=True)
    mimage = models.FileField(upload_to='materialimage',blank=True,null=True)
    price = models.IntegerField(blank=True,null=True)
    weights = models.IntegerField(blank=True,null=True)
    nomc = models.IntegerField(blank=True,null=True)
    proddesc = models.TextField(null=True,blank=True)
    # acitive = models.BooleanField(default=True)

    def __str__(self):
        return self.provider.fname + ' -> ' + self.mname