from django.contrib import admin
from django.urls import path, re_path
from Campaign_Banner import views

urlpatterns = [ 
     re_path(r'^api/campban$', views.CamBan_list), 
     re_path(r'^api/campban/(?P<pk>[0-9]+)$', views.CamBan_detail),
     re_path(r'^api/CampaigndeleteAll$', views.CamDelete),
]