from dataclasses import fields
from django import forms
from django.contrib import forms

# Register your models here.
from .models import InvestorsDetsModel

class InvestorsDetsForm(forms.ModelAdmin):
    class meta:
        models=InvestorsDetsModel
        fields=["MTUSER_ID","EMAIL","MODULE","INVESTOR_SNO","INV_TEAM_NAME","TEAM_POSITION","FB_LINK","INSTA_LINK","LINKEDIN_LINK","BIO","PRO_PIC","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE"]