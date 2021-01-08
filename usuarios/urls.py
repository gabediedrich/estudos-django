from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home),
    path('user_home/', views.home, name="user_home"),
    path('add_user/', views.add_user, name='add_user'),
]