
from django.contrib import admin
from django.urls import path,re_path,include
from app02 import views


urlpatterns = [
    # path('login/', views.login),
    re_path('business/$', views.business),
    re_path('host/$', views.host),
    re_path('test_ajax/$', views.test_ajax),
    # re_path('useredit-(?P<nid>\d+)/', views.user_edit),
    # path('user_group/', views.user_group),
]
