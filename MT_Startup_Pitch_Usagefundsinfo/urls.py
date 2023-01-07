from django.contrib import admin
from django.urls import path, re_path
from MT_Startup_Pitch_Usagefundsinfo import views

urlpatterns = [ 
    re_path(r'^api/ptusage$', views.Usagefundsinfo_list),
    re_path(r'^api/ptusage/(?P<pk>[0-9]+)$', views.Usagefundsinfo_detail),
]