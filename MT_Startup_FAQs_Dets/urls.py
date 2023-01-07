from django.contrib import admin
from django.urls import path, re_path
from MT_Startup_FAQs_Dets import views

urlpatterns = [ 
    re_path(r'^api/FAQs/$', views.FAQs_list),
    re_path(r'^api/FAQs/([0-9])$', views.FAQs_detail),
]