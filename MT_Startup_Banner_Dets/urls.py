from django.contrib import admin
from django.urls import path, re_path
from MT_Startup_Banner_Dets import views

urlpatterns = [ 
    re_path(r'^api/Banner/$', views.Banner_list),
    re_path(r'^api/Banner/([0-9])$', views.Banner_detail),
]