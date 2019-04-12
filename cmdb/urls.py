
from django.contrib import admin
from django.urls import path,re_path,include
from cmdb import views


urlpatterns = [
    path('login/', views.login),
]
