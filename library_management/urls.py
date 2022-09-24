from django.urls import path

from library_management.views import  AccountCreateView, Book, Home, Login, Logout, Register, VerifyOTP

urlpatterns = [
    path('register',Register.as_view(),name='register'),
    path('verify_otp',VerifyOTP.as_view(),name='verify_otp'),
    path('',Home.as_view(),name='home'),
    path('book',Book.as_view(),name='book'),
    path('login',Login.as_view(),name='login'),
    path('logout',Logout,name='logout'),
    path('register_api/',AccountCreateView.as_view(),name='register_api')
]
