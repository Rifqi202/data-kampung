from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    # path('login/', views.login, name='login'),
#     path('daftarwarga', views.daftarwarga, name='daftarwarga'),
]
