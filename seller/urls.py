from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.signin,name='signin'),
    path('Index/', views.index,name='index'),
    path('SignUp/', views.signup,name='signup'),
    path('OTP/', views.otp,name='otp'),
    path('Logout/', views.logout,name='logout'),
    path('Forgot_Password/', views.forgot,name='forgot'),
    path('Change_Password/', views.changepswd,name='changepswd'),
    path('My_Profile/', views.profile,name='profile'),
    path('Service/', views.service,name='service'),
    path('My_Service/', views.myservice,name='myservice'),
    path('delete-service/<int:pk>',views.delete_service,name='delete-service'),
    path('inactive-service/<int:pk>',views.inactive_service,name='inactive-service'),
    path('active-service/<int:pk>',views.active_service,name='active-service'),
    path('edit-service/<int:pk>',views.edit_service,name='edit-service'),
    path('View-client-booking/',views.view_client_booking,name='view-client-booking'),
   


    path('view-client-book/<int:pk>',views.view_client_book,name='view-client-book'),
    path('order_dispetch/<int:pk>',views.order_dispetch,name='order_dispetch'),
    path('order_ofd/<int:pk>',views.order_ofd,name='order_ofd'),
    path('order_dvd/<int:pk>',views.order_dvd,name='order_dvd'),

]
