from django.shortcuts import render,redirect
from django.views import View
from collage.models import CollageModel
from django.contrib import messages
from library_management.models import UserAccount
# Create your views here.

class CollageView(View):

    def get(self, request):
        return render(request,'collage_register.html')

    def post(self, request):
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        number = request.POST['mobile_number']
        type = request.POST['type']
        profile_pic = request.POST['profile_pic']
        user = UserAccount.objects.filter(email=email).first()
        user.first_name = first_name
        user.last_name = last_name
        user.mobile_number = number
        user.profile_pic = profile_pic
        user.save()
        CollageModel.objects.create(
            user = user,
            type = type
        )
        context = {
            'email':email,
            'type' :type
        }
        
        request.session['context'] = context
        return redirect('register1')

class Register1(View):

    def get(self, request):
        return render(request,'collage_register1.html')

    def post(self, request):
        email = request.POST['email']
        dob = request.POST['dob']
        address = request.POST['address']
        gender = request.POST['gender']
        student_class = request.POST.get('student_class','')
        dept = request.POST.get('dept','')
        user = UserAccount.objects.filter(email=email).first()
        user.dob = dob
        user.address = address
        user.gender = gender
        
        user_data = CollageModel.objects.filter(user__email=email).first()
        user_data.dept = dept
        user_data.student_class = student_class
        user_data.save()
        user.is_created = True
        user.save()
        messages.add_message(request,messages.WARNING, f"Account Register SuccessFully")
        return redirect('home')
