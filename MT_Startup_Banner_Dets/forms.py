from dataclasses import fields
from django import forms
from django.contrib import forms

# Register your models here.
from .models import BannerModel

class BannerForm(forms.ModelAdmin):
    class meta:
        models=BannerModel
        fields=["MTUSER_ID","EMAIL","MODULE","BANNER_SNO","BANNER_IMAGE","BANNER_VIDEO","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE"]