from django.contrib import admin
from django.urls import path, re_path
from MT_Startup_Investors_Dets import views

urlpatterns = [ 
    re_path(r'^api/InvestorsDets/$', views.InvestorsDets_list),
    re_path(r'^api/InvestorsDets/([0-9])$', views.InvestorsDets_detail),
]