from django.contrib import admin
from django.urls import path, re_path
from MT_Investor_Verifiy_Nationality import views

urlpatterns = [ 
    re_path(r'^api/inv_nationality$', views.Nationality_list),
    re_path(r'^api/inv_nationality/(?P<pk>[0-9]+)$', views.Nationality_detail),
]