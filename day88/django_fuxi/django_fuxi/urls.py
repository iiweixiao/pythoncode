"""django_fuxi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('init/', views.init),
    path('info/list/', views.info_list),
    path('add/user/', views.add_user),
    path('modelform/add/user/', views.modelform_add_user),
    path('user/delete/', views.delete_user),
    path('user/<int:nid>/edit/', views.edit_user),
]
