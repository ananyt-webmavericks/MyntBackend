from django.contrib import admin
from django.urls import path, re_path
from MT_Startup_Pitch_Productinfo import views

urlpatterns = [ 
    re_path(r'^api/ptproduct$', views.Productinfo_list),
    re_path(r'^api/ptproduct/(?P<pk>[0-9]+)$', views.Productinfo_detail),
]