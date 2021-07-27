
from os import name
from django.urls import path
from . import views

urlpatterns = [
   path('',views.index,name='index.html'),
   path('about',views.about,name='about'),
   path('index2',views.index2,name='index2')
]
