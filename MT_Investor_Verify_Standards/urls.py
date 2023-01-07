from django.contrib import admin
from django.urls import path, re_path
from MT_Investor_Verify_Standards import views

urlpatterns = [ 
    re_path(r'^api/inv_terms$', views.Standards_list),
    re_path(r'^api/inv_terms/(?P<pk>[0-9]+)$', views.Standards_detail),
]