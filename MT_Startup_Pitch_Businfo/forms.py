from dataclasses import fields
from django import forms
from django.contrib import forms

# Register your models here.
from .models import BusinfoModel

class BusinfoForm(forms.ModelAdmin):
    class meta:
        models=BusinfoModel
        fields=["ID","MTUSER_ID","EMAIL","MODULE","PIT_BSMODEL_HEADER","PIT_BSMODEL_BODY","PIT_BSMODEL_IMAGE","PIT_BSMODEL_VIDEO","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE"]