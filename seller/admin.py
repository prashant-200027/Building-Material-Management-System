from django.contrib import admin

from seller.models import Service, User

# Register your models here.

admin.site.register(User)
admin.site.register(Service)

admin.site.site_header = "E-Civil Admin"
admin.site.site_title = "E-Civil Admin Portal"
admin.site.index_title = "Welcome to E-Civil Portal"
