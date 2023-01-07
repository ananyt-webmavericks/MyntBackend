from django.contrib import admin
from django.urls import path, re_path
from MT_Startup_Pitch_Solution import views

urlpatterns = [ 
    re_path(r'^api/solution$', views.Solution_list),
    re_path(r'^api/solution/(?P<pk>[0-9]+)$', views.Solution_detail),
]