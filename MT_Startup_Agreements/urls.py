from django.contrib import admin
from django.urls import path, re_path
from MT_Startup_Agreements import views

urlpatterns = [ 
    re_path(r'^api/Agreements/$', views.Agreements_list),
    re_path(r'^api/Agreements/([0-9])$', views.Agreements_detail),
]