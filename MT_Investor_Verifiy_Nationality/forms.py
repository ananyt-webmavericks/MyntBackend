from dataclasses import fields
from django import forms
from django.contrib import forms

# Register your models here.
from .models import NationalityModel

class NationalityForm(forms.ModelAdmin):
    class meta:
        models=NationalityModel
        fields=["MTUSER_ID","EMAIL","MODULE",
                "NATIONALITY","STATUS","COMMENTS",
                "DESCRIPTION","CREATED_USER","CREATED_DATE",
                "MODIFIED_USER","MODIFIED_DATE"]