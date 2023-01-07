from django.contrib import admin
from django.urls import path, re_path
from MT_Startup_Pitchinfo import views

urlpatterns = [ 
    re_path(r'^api/uploadpitch$', views.Pitchinfo_list),
    re_path(r'^api/uploadpitch/([0-9])$', views.Pitchinfo_detail),
]