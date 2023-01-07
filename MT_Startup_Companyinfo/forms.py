from dataclasses import fields
from django import forms
from django.contrib import forms

# Register your models here.
from .models import CompanyinfoModel

class CompanyinfoForm(forms.ModelAdmin):
    class meta:
        models=CompanyinfoModel
        fields=["ID","MTUSER_ID","EMAIL","MODULE","COUNTRY","STATE","CITY","PINCODE","ADDRESS","COMPANY_WEBSITE","FB_LINK","INSTA_LINK","LINKEDIN_LINK","LEGAL_NAME","CIN_NUMBER","DATE_OF_INCORPORATATION","INCORPORATION_TYPE","ABOUT_COMPANY","AMOUNT_INVESTED","NO_OF_EMPLOYEES","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE"]