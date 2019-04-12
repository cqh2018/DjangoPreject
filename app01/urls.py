
from django.contrib import admin
from django.urls import path,re_path,include
from app01 import views


urlpatterns = [
    path('login/', views.login),
    path('index/', views.index),
    path('user_info/', views.user_info),
    re_path('userdetail-(?P<nid>\d+)/', views.user_detail),
    re_path('userdel-(?P<nid>\d+)/', views.user_del),
    re_path('useredit-(?P<nid>\d+)/', views.user_edit),
    # path('user_group/', views.user_group),
    path('orm/', views.orm),
]
