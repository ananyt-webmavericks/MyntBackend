from django.contrib import admin
from django.urls import path, re_path
from MT_Startup_Pitch_Visioninfo import views

urlpatterns = [ 
    re_path(r'^api/ptvision$', views.Visioninfo_list),
    re_path(r'^api/ptvision/(?P<pk>[0-9]+)$', views.Visioninfo_detail),
]