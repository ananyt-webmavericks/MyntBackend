from dataclasses import fields
from django import forms
from django.contrib import forms

# Register your models here.
from .models import PressinfoModel

class PressinfoForm(forms.ModelAdmin):
    class meta:
        models=PressinfoModel
        fields=["MTUSER_ID","EMAIL","MODULE","PRESS_SNO","PRESS_HEADER","PRESS_BODY","PRESS_IMAGE","PRESS_VIDEO","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE"]