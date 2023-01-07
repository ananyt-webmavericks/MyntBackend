from django.contrib import admin
from django.urls import path, re_path
from MT_Startup_Pitch_Businfo import views

urlpatterns = [ 
    re_path(r'^api/ptbusiness$', views.Businessinfo_list),
    re_path(r'^api/ptbusiness/(?P<pk>[0-9]+)$', views.Businessinfo_detail),
]