
from django.contrib import admin
from django.urls import path,re_path,include
from admincenter import views


urlpatterns = [
    # path('login/', views.login),
    # re_path('business/$', views.business),
    path('downloadTest/', views.downloadTest),
    path('download/', views.download),
    path('index/', views.index),
]
