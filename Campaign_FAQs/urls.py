from django.contrib import admin
from django.urls import path, re_path
from Campaign_FAQs import views
 
 
urlpatterns = [
    re_path(r'^api/camfaq$', views.CampFAQ_list),
    re_path(r'^api/camfaq/(?P<pk>[0-9]+)$', views.CampFAQ_detail),
]