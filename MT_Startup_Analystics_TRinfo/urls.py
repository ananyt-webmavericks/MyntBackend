from django.contrib import admin
from django.urls import path, re_path
from MT_Startup_Analystics_TRinfo import views

urlpatterns = [ 
    re_path(r'^api/Analystics/$', views.Analystics_list),
    re_path(r'^api/Analystics/([0-9])$', views.Analystics_detail),
]