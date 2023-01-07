from dataclasses import fields
from django import forms
from django.contrib import forms

# Register your models here.
from .models import CamFAQsModel

class CamFAQsForm(forms.ModelAdmin):
    class meta:
        models=CamFAQsModel
        fields=["ID","MTUSER_ID","EMAIL","MODULE",
                "CFAQ_SNO",
                "CFAQ_QUESTION", 
                "CFAQ_QANSWER", 
                "STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE"]