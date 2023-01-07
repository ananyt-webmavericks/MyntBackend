from dataclasses import fields
from django import forms
from django.contrib import forms

# Register your models here.
from .models import CampaignBannerModel

class CampaignBannerForm(forms.ModelAdmin):
    class meta:
        models=CampaignBannerModel
        fields=["ID","MTUSER_ID","EMAIL","MODULE",
                "CAM_BAN_IMAGE","CAM_BAN_VIDEO",
                "STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE",
                "MODIFIED_USER","MODIFIED_DATE"]