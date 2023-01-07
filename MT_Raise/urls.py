from django.contrib import admin
from django.urls import path, re_path
from MT_Raise import views
 
 
urlpatterns = [
    re_path(r'^api/raise$', views.Raise_list),
    re_path(r'^api/raise/(?P<pk>[0-9]+)$', views.Raise_detail),
]