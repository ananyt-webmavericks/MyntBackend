from django.contrib import admin
from django.urls import path, re_path
from Campaign_Press import views

urlpatterns = [ 
     re_path(r'^api/campress$', views.CampaignPress_list), 
     re_path(r'^api/campress/(?P<pk>[0-9]+)$', views.CampaignPress_detail),
]