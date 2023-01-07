from django.contrib import admin
from django.urls import path, re_path
from MT_Startup_Pitch_Tractioninfo import views

urlpatterns = [ 
    re_path(r'^api/pttransaction$', views.Tractioninfo_list),
    re_path(r'^api/pttransaction/(?P<pk>[0-9]+)$', views.Tractioninfo_detail),
]