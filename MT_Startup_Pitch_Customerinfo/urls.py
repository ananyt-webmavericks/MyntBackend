from django.contrib import admin
from django.urls import path, re_path
from MT_Startup_Pitch_Customerinfo import views

urlpatterns = [ 
    re_path(r'^api/ptcustomer$', views.Customerinfo_list),
    re_path(r'^api/Customerinfo/(?P<pk>[0-9]+)$', views.Customerinfo_detail),
]