# from django.contrib import admin
from django.urls import path

from . import views
urlpatters: [
    # path('', views.index),
     path('login', views.login),
    
]
