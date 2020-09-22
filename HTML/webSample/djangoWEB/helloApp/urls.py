from django.contrib import admin
from django.urls import path
from helloApp import views

urlpatterns = [
    path('index/', views.index),
    path('hi/', views.hi),
    path('login/', views.login, name='login'),
]
