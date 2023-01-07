from django.contrib import admin
from django.urls import path, re_path
from MT_Startup_Pitch_PotentialReturnsinfo import views

urlpatterns = [ 
    re_path(r'^api/potreturns$', views.PotentialReturnsinfo_list),
    re_path(r'^api/potreturns/(?P<pk>[0-9]+)$', views.PotentialReturnsinfo_detail),
]