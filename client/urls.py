from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.client_index,name="client_index"),
    path('client-view-service/<int:pk>',views.view_service,name="client-view-service"),
    path('Client-Signin/', views.client_signin, name='client_signin'),
    path('Client-Signup/', views.client_signup, name='client_signup'),
    path('Client-Index/', views.client_index, name='client_index'),
    path('Client-OTP/', views.client_otp, name='client_otp'),
    path('Client-Logout/', views.client_logout, name='client_logout'),
    path('Client-Forgot-password/', views.client_forgot, name='client_forgot'),
    path('Add-client-details/', views.add_client_details, name='add_client_details'),
    path('Book-Product/<int:pk>', views.book_prod, name='book_prod'),

    path('Book-Product/paymenthandler/<int:pk>', views.paymenthandler, name='paymenthandler'),
    path('View-Orders', views.view_order, name='view_order'),
    path('Order-Detail', views.order_detail, name='order_detail'),
    # path('Client-Dashboard/', views.client_dashboard, name='client_dashboard'),
]