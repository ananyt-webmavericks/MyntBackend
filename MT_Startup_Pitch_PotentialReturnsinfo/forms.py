from dataclasses import fields
from django import forms
from django.contrib import forms

# Register your models here.
from .models import Startup_Pitch_PotentialReturnsinfoModel

class PotentialReturnsinfoForm(forms.ModelAdmin):
    class meta:
        models=Startup_Pitch_PotentialReturnsinfoModel
        fields=["ID","MTUSER_ID","EMAIL","MODULE","PIT_POTRET_HEADER","PIT_POTRET_BODY","PIT_POTRET_IMAGE","PIT_POTRET_VIDEO","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE"]