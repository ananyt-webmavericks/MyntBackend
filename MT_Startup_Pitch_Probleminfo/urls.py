from django.contrib import admin
from django.urls import path, re_path
from MT_Startup_Pitch_Probleminfo import views

urlpatterns = [ 
     re_path(r'^api/createpitch$', views.Probleminfo_list), 
     re_path(r'^api/createpitch/(?P<pk>[0-9]+)$', views.Probleminfo_detail),
]