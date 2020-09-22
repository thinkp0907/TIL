from django.contrib import admin
from django.urls import path
from BbsApp import views

urlpatterns = [
    path('index/', views.loginForm, name='index'),
    path('registerForm/', views.registerForm, name="registerForm"),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('bbs_list/', views.board, name='bbs_list'),
    path('bbs_registerForm/', views.bbsRegisterForm, name='bbs_registerForm'),
    path('bbs_register/', views.bbsRegister, name='bbs_register'),
    path('fetch/<int:id>', views.fetch, name='fetch'),
    path('bbs_remove/', views.remove, name="bbs_remove"),
]
