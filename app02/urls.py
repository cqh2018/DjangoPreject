
from django.contrib import admin
from django.urls import path,re_path,include
from app02 import views


urlpatterns = [
    # path('login/', views.login),
    re_path('business/$', views.business),
    re_path('host/$', views.host),
    re_path('test_ajax/$', views.test_ajax),
    re_path('edit_ajax/$', views.edit_ajax),
    path('app/', views.app),
    path('ajax_add_app/', views.ajax_add_app),
    path('ajax_edit_app/', views.ajax_edit_app),
    path('ajax_delete_app/', views.ajax_delete_app),
]
