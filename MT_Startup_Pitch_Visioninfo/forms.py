from dataclasses import fields
from django import forms
from django.contrib import forms

# Register your models here.
from .models import VisioninfoModel

class VisioninfoForm(forms.ModelAdmin):
    class meta:
        models=VisioninfoModel
        fields=["ID","MTUSER_ID","EMAIL","MODULE","PIT_VSN_HEADER","PIT_VSN_BODY","PIT_VSN_IMAGE","PIT_VSN_VIDEO","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE"]