from django.contrib import admin
from django.urls import path, re_path
from MT_Investor_Payment import views

urlpatterns = [ 
    re_path(r'^api/Payment/$', views.Payment_list),
    re_path(r'^api/Payment/([0-9])$', views.Payment_detail),
]