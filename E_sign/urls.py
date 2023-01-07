from django.contrib import admin
from django.urls import path, re_path
from E_sign import views

urlpatterns = [ 
     re_path(r'^api/esign$', views.ESign_list), 
     re_path(r'^api/esign/(?P<pk>[0-9]+)$', views.ESign_details),
]