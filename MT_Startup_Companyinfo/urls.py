

from django.contrib import admin
from django.urls import re_path,include 
from MT_Startup_Companyinfo import views

urlpatterns = [ 
    
    re_path(r'^api/company_info$', views.companyinfo_list),
    re_path(r'^api/company_info/(?P<pk>[0-9]+)$', views.companyinfo_details), 

     
]