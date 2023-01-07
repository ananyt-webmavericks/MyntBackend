from dataclasses import fields
from django import forms
from django.contrib import forms

# Register your models here.
from .models import StandardsModel

class Investor_DashboardForm(forms.ModelAdmin):
    class meta:
        models=StandardsModel
        fields=["MTUSER_ID","EMAIL","MODULE",
                "INV_RISK",
                "INV_LIMITED_TRANSFER",
                "INV_DIVERSIFICATION",
                "INV_CANCELLATION",
                "INV_RESEARCH",
                "STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE"]
        
        
        
        