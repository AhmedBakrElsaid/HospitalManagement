from django.urls import path
from .views import about,home,contact

urlpatterns = [
    path('about/',about,name='about'),
    path('home/',home,name='home'),
    path('contact/',contact,name='contact'),
]

