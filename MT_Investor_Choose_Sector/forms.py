from dataclasses import fields
from django import forms
from django.contrib import forms

# Register your models here.
from .models import Choose_SectorModel

class Choose_SectorForm(forms.ModelAdmin):
    class meta:
        models=Choose_SectorModel
        fields=["MTUSER_ID","EMAIL","MODULE",
                "INV_CHOOSE_SECTOR","STATUS",
                "COMMENTS","DESCRIPTION","CREATED_USER",
                "CREATED_DATE","MODIFIED_USER","MODIFIED_DATE"]