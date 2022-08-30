"""day108 URL Configuration

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
    # path('admin/', admin.site.urls),

    path('', views.index),
    path('test/', views.test),
    path('up/list/', views.up_list),
    path('video/list/', views.video_list),
    path('video/list/refresh/', views.refresh),
    path('heji/', views.heji),
    path('up/video/list/', views.up_video_list),
    path('<int:nid>/edit/', views.up_edit),
    path('<int:nid>/delete/', views.up_delete),
    path('test/ajax/', views.test_ajax),
    path('test/ajax/test/', views.test_ajax_test),
    path('test/ajax/form/', views.ajax_form),


]
