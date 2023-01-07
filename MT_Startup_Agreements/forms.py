from dataclasses import fields
from django import forms
from django.contrib import forms

# Register your models here.
from .models import AgreementsModel

class AgreementsForm(forms.ModelAdmin):
    class meta:
        models=AgreementsModel
        fields=["MTUSER_ID","EMAIL","MODULE","ESIGN_DOC","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE"]