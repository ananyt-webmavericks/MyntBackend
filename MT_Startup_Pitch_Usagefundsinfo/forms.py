from dataclasses import fields
from django import forms
from django.contrib import forms

# Register your models here.
from .models import UsagefundsinfoModel

class UsagefundsinfoForm(forms.ModelAdmin):
    class meta:
        models=UsagefundsinfoModel
        fields=["ID","MTUSER_ID","EMAIL","MODULE","PIT_USAGE_HEADER","PIT_USAGE_BODY","PIT_USAGE_IMAGE","PIT_USAGE_VIDEO","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE"]