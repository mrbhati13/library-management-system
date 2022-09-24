
import re
from django.shortcuts import render,redirect
from django.views import View
from book.models import BookModel

from library_management.models import UserAccount
# Create your views here.

class BookRegistration(View):

    def get(self, request):
        return render(request,'book_register.html')

    def post(self, request):
        email = request.POST['email']
        first_name = request.POST.get('first_name','')
        last_name = request.POST.get('last_name','')
        mobile_number = request.POST.get('mobile_number','')
        profile_pic = request.POST.get('profile_pic','')
        dob = request.POST.get('dob','')
        address = request.POST.get('address','')
        gender = request.POST.get('gender','')
        user = UserAccount.objects.filter(email=email).first()
        user.first_name = first_name
        user.last_name = last_name
        user.mobile_number = mobile_number
        user.profile_pic = profile_pic
        user.dob = dob
        user.address = address
        user.gender = gender
        user.is_created=True
        user.save()
        context={
            "user":user.email
        }
        request.session['context']=context
        return redirect('book_register1')

class BookRegister1(View):
    def get(self, request):
        return render(request, 'book_register1.html')

    def post(self, request):
        title = request.POST.get('title','')
        topic = request.POST.get('topic','')
        genre = request.POST.get('genre','')
        book  = request.POST.get('book','')
        book_cover = request.POST.get('book_cover','')
        length = request.POST.get('length','')
        publisher = request.POST.get('publisher','')
        summary = request.POST.get('summary','')
        language = request.POST.get('language','')
        edition = request.POST.get('edition','')
        formate = request.POST.get('formate','')
        user_ = request.session['context']['user']
        print('**********',user_)
        user = UserAccount.objects.filter(email=user_).first()
        book_data = BookModel.objects.create(
            title=title,
            author=user,
            topic=topic,
            genre=genre,
            book=book,
            book_cover=book_cover,
            length=length,
            publisher=publisher,
            summary=summary,
            language=language,
            edition=edition,
            formate=formate,
        )
        return redirect('home')