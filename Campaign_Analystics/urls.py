from django.contrib import admin
from django.urls import path, re_path
from Campaign_Analystics import views
 
 
urlpatterns = [
    re_path(r'^api/camAnalytics$', views.CampAnalytics_list),
    re_path(r'^api/camAnalytics/(?P<pk>[0-9]+)$', views.CampAnalytics_detail),
]