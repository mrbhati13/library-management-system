from django.urls import path

from book.views import BookRegister1, BookRegistration

urlpatterns = [
        path('book_register',BookRegistration.as_view(),name='book_register'),
        path('bookregister1',BookRegister1.as_view(),name='book_register1')
]
