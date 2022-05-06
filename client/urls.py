from django import views
from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.client_index,name='client-index'),

    path('client-view-service/<int:pk>', views.client_view_service,name='client-view-service'),
    path('Client-Index/', views.client_index, name='client_index'),

    path('client-profile/', views.client_profile,name='client_profile'),
    path('Client-Signin/', views.client_signin, name='client_signin'),
    path('Client-Signup/', views.client_signup, name='client_signup'),
    path('Client-OTP/', views.client_otp, name='client_otp'),
    path('Client-Logout/', views.client_logout, name='client_logout'),
    path('Client-Forgot-password/', views.client_forgot, name='client_forgot'),

    path('client-contact/', views.client_contact, name='client_contact'),
    path('client-service/', views.client_service, name='client_service'),
    path('client-about/', views.client_about, name='client_about'),

    path('Book-Product/<int:pk>', views.book_prod, name='book_prod'),
    path('Book-Product/paymenthandler/<int:pk>', views.paymenthandler, name='paymenthandler'),

    path('View-Orders', views.view_order, name='view_order'),
    path('Order-Detail/<int:pk>', views.order_detail, name='order_detail'),
    path('Order-status/<int:pk>', views.order_status, name='order_status'),
]