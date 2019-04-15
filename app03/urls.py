
from django.contrib import admin
from django.urls import path,re_path,include
from app03 import views


urlpatterns = [
    # path('login/', views.login),
    # re_path('business/$', views.business),
    path('fenye/', views.fenye),
]
