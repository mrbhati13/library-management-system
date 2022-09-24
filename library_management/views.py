
from django.shortcuts import render,redirect
from django.views import View
from library_management.models import UserAccount
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from library_management.serializers import AccountCreateSerializer
from django.http import JsonResponse
from library_management.utils import get_otp
from django.contrib.auth import authenticate,login,logout
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from project.settings import EMAIL_HOST_USER
import pyotp
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Register(View):
    def get(self, request):
        return render(request,'register.html')

    def post(self, request):
        print("******************register")
        email = request.POST['email'].lower()
        user_type = request.POST['user_type']
        password = request.POST['password']
        
        if UserAccount.objects.filter(email=email).exists():
            messages.add_message(request,messages.ERROR, "You are account is already exists")
            return redirect('register')
        else:
            otp = get_otp()
            context = {
                'email':email,
                "user_type":user_type,
                "password":password,
                "otp": otp['otp'],
                "secret":otp['secret']
            }
            html_content = render_to_string('otp_send.html',context)
            emailMessage = EmailMultiAlternatives(subject="OTP", body=html_content,      
                    from_email=EMAIL_HOST_USER,                                           
                    to=[email])
            emailMessage.attach_alternative(html_content, "text/html")
            emailMessage.send(fail_silently=False)
            message =  messages.add_message(request,messages.SUCCESS, f"OTP has been sended your email {email}")
            request.session['context']=context
            return JsonResponse({'success':True},status=200)

class VerifyOTP(View):

    def get(self, request):
        return render(request,'verify_otp.html')

    def post(self, request):
        try:
            email = request.POST['email']
            user_type = request.POST['user_type']
            password = request.POST['password']
            otp = request.POST['otp']
            secret = request.POST['secret']
            verify_otp = pyotp.TOTP(secret, interval=600).verify(otp)
            if verify_otp:
                UserAccount.objects.create(
                    email=email,
                    user_type=user_type,
                    password=make_password(password)
                )
                messages.add_message(request,messages.SUCCESS, f"OTP Verification SuccessFully")
                if user_type == 'COLLAGE':
                    return redirect('collage_register')
                if user_type == "BOOK":
                    return redirect('book_register')
                if user_type == "LIBRARIAN":
                    return redirect()
            messages.add_message(request,messages.WARNING, f"OTP Verification Failed")
            return redirect('register')
        except Exception as e:
            messages.add_message(request,messages.WARNING, str(e))
            return redirect('register')


class Home(View):
    def get(self, request):
        return render(request,'home.html')

class Book(View):

    def get(self, request):
        return render(request, 'book.html')

class Login(View):
    
    def get(self, request):
        return render(request, 'signin.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password, is_created=True)
        if user:
            login(request, user)
            return redirect('home')
        return redirect('login')

def Logout(request):
    logout(request)
    return redirect('home')


class AccountCreateView(APIView):
    serilaizer_classes = AccountCreateSerializer

    def post(self, request):
        print("******************register_api")
        serializer = self.serilaizer_classes(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors.items(),status=status.HTTP_400_BAD_REQUEST)