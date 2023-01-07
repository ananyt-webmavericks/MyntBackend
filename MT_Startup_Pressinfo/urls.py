from django.contrib import admin
from django.urls import path, re_path
from MT_Startup_Pressinfo import views

urlpatterns = [ 
    re_path(r'^api/Pressinfo/$', views.Pressinfo_list),
    re_path(r'^api/Pressinfo/([0-9])$', views.Pressinfo_detail),
]