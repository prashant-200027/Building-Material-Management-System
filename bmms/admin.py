from django.contrib import admin

from bmms.models import Service, User

# Register your models here.

admin.site.register(User)
admin.site.register(Service)