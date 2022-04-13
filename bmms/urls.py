from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('Signup/', views.signup, name='signup'),
    path('Index/', views.index, name='index'),
    path('OTP/', views.otp, name='otp'),
    path('Logout/', views.logout, name='logout'),
    path('Forgot-password/', views.forgot, name='forgot'),
    path('Profile/', views.profile, name='profile'),
    path('Change-Password/',views.changepswd,name='changepswd'),
    path('Service/',views.service,name='service'),
    path('My-Service/',views.myservice,name='myservice'),
    path('delete-service/<int:pk>',views.delete_service,name='delete-service'),
    path('inactive-service/<int:pk>',views.inactive_service,name='inactive-service'),
    # path('active-service/<int:pk>',views.active_service,name='active-service'),
    path('edit-service/<int:pk>',views.edit_service,name='edit-service'),
]

         