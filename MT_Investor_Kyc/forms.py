from dataclasses import fields
from django import forms
from django.contrib import forms

# Register your models here.
from .models import Investor_KycModel

class KycForm(forms.ModelAdmin):
    class meta:
        models=Investor_KycModel
        fields=["MTUSER_ID","EMAIL","MODULE",
                "INV_COUNTRYCODE",
              "INV_MOBILE_NUMBER",
              "INV_OTP",
              "INV_PAN",
              "INV_DOB",
              "INV_BANKACCNO",
              "INV_IFSCCODE",
                "STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE"]