from django.contrib import admin
from django.urls import path, re_path
from MT_Startup_Teaminfo import views
 
 
urlpatterns = [
    re_path(r'^api/teaminfo$', views.Teaminfo_list),
    re_path(r'^api/teaminfo/(?P<pk>[0-9]+)$', views.Teaminfo_detail),
]