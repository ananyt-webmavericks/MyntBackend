from django.contrib import admin
from django.urls import path, re_path
from MT_Investor_Kyc import views

urlpatterns = [ 
    re_path(r'^api/investordetails$', views.kyc_list),
    re_path(r'^api/investordetails/(?P<pk>[0-9]+)$', views.kyc_detail),
]