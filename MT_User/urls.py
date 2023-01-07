from django.contrib import admin
from django.urls import re_path,include 
from MT_User import views

urlpatterns = [ 
    
    re_path(r'^api/mt_user$', views.mtuser_list),
    re_path(r'^api/mt_user/(?P<pk>[0-9]+)$', views.mtuser_detail),
    re_path(r'^api/userlogin$', views.userlogin ),
    re_path(r'^api/chkEmailExist$', views.chkEmailExist ) 

     
]