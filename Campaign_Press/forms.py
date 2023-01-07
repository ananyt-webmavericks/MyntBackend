from dataclasses import fields
from django import forms
from django.contrib import forms

# Register your models here.
from .models import CampPressModel

class CampaignPressForm(forms.ModelAdmin):
    class meta:
        models=CampPressModel
        fields=["ID","MTUSER_ID","EMAIL","MODULE",
                "CAMP_PRESS_HEADER","CAMP_PRESS_BODY","CAMP_PRESS_IMAGE","CAMP_PRESS_VIDEO",
                "STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE",
                "MODIFIED_USER","MODIFIED_DATE"]