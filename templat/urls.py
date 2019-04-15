
from django.contrib import admin
from django.urls import path,re_path,include
from templat import views


urlpatterns = [
    # path('login/', views.login),
    # re_path('business/$', views.business),
    path('templat1/', views.template1),
    path('templat2/', views.template2),
    path('templat3/', views.template3),
    path('templat4/', views.template4),
]
