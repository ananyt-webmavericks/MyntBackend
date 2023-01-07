from django.contrib import admin
from django.urls import path, re_path
from Campaign_Investors import views
 
 
urlpatterns = [
    re_path(r'^api/caminvest$', views.CampInvestor_list),
    re_path(r'^api/caminvest/(?P<pk>[0-9]+)$', views.CampInvestor_detail),
    re_path(r'^api/campaignAllDets$', views.CampaignAll_list),
     re_path(r'^api/camAllDets$', views.CampaignAll_Details),
    # re_path(r'^api/campaignAllDets/(?P<pk>[0-9]+)$', views.Camp_Individual),
    
]