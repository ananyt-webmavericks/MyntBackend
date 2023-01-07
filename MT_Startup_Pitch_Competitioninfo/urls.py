from django.contrib import admin
from django.urls import path, re_path
from MT_Startup_Pitch_Competitioninfo import views

urlpatterns = [ 
    re_path(r'^api/ptcomp$', views.Competitioninfo_list),
    re_path(r'^api/ptcomp/(?P<pk>[0-9]+)$', views.Competitioninfo_detail),
]