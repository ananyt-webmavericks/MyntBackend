from dataclasses import fields
from django import forms
from django.contrib import forms

# Register your models here.
from .models import ProductinfoModel

class ProductinfoForm(forms.ModelAdmin):
    class meta:
        models=ProductinfoModel
        fields=["ID","MTUSER_ID","EMAIL","MODULE","PIT_PROD_HEADER","PIT_PROD_BODY","PIT_PROD_IMAGE","PIT_PROD_VIDEO","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE"]