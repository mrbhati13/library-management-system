from django.urls import path

from collage.views import CollageView, Register1

urlpatterns = [
    path('collage_register',CollageView.as_view(),name='collage_register'),
    path('register1',Register1.as_view(),name='register1'),
]
