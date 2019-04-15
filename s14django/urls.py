"""s14django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cmdb/', include('cmdb.urls')),
    path('app01/', include('app01.urls')),
    path('app02/', include('app02.urls')),
    path('app03/', include('app03.urls')),
    path('templat/', include('templat.urls')),
    path('admincenter/', include('admincenter.urls')),
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # url(r'^h.html/', views.home),
#     path('login/', views.login),
#     # path('home/', views.home),
#     path('del_host/', views.del_host),
#     path('dafda/', views.index,name='indexx'),
#     path('home/', views.Home.as_view()),
#     # path('detail/', views.detail),
#     # re_path('detail-(\d+)-(\d+).html', views.detail),
#     # re_path('detail-(?P<nid>\d+)-(?P<uid>\d+).html', views.detail),
#     re_path('detail-(?P<nid>\d+).html', views.detail),
# ]
