from django.contrib import admin
from django.urls import path

from Application import views

urlpatterns = [
    path('',views.home,name='home'),
    path('accounts/register/',views.register,name='register'),
]
