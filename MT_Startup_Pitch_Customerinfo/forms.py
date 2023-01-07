from dataclasses import fields
from django import forms
from django.contrib import forms

# Register your models here.
from .models import CustomerinfoModel

class CustomerinfoForm(forms.ModelAdmin):
    class meta:
        models=CustomerinfoModel
        fields=["ID","MTUSER_ID","EMAIL","MODULE","PIT_CUST_HEADER","PIT_CUST_BODY","PIT_CUST_IMAGE","PIT_CUST_VIDEO","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE"]