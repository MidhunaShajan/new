from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('get-courses/', views.get_courses, name='get_courses'),
    path('',views.home,name='home'),
    path('reg',views.firstregister,name='firstregister'),
    path('login',views.login,name='login'),
    path('new',views.new,name='new'),
    path('logout',views.logout,name='logout'),
]