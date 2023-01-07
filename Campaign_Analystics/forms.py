from dataclasses import fields
from django import forms
from django.contrib import forms

# Register your models here.
from .models import CampaignAnalyticsModel

class CampaignAnalyticsForms(forms.ModelAdmin):
    class meta:
        models=CampaignAnalyticsModel
        fields=["ID","MTUSER_ID","EMAIL","MODULE",
                "ANLYSTICS_IMAGE",
      "ANLYSTICS_GROWTHPROFIT",
      "ANLYSTICS_MONRECURRING",
      "ANLYSTICS_CUSTCHURNRATE",
      "ANLYSTICS_MONACTIVEUSER",
      "ANLYSTICS_CACRATIO", 
                "STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE"]