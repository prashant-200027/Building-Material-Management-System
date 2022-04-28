from multiprocessing.connection import Client
from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(ClientUser)
admin.site.register(Booking)
