from django.contrib import admin
from django.urls import path, re_path
from MT_Investor_Choose_Sector import views

urlpatterns = [  
    re_path(r'^api/Choose_Sector$', views.Choose_Sector_list),
    re_path(r'^api/Choose_Sector/(?P<pk>[0-9]+)$', views.Choose_Sector_detail),
]