from dataclasses import fields
from django import forms
from django.contrib import forms

# Register your models here.
from .models import TractioninfoModel

class TractioninfoForm(forms.ModelAdmin):
    class meta:
        models=TractioninfoModel
        fields=["ID","MTUSER_ID","EMAIL","MODULE","PIT_TRANS_HEADER","PIT_TRANS_BODY","PIT_TRANS_IMAGE","PIT_TRANS_VIDEO","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE"]