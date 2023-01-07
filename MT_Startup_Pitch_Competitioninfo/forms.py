from dataclasses import fields
from django import forms
from django.contrib import forms

# Register your models here.
from .models import CompetitioninfoModel

class CompetitioninfoForm(forms.ModelAdmin):
    class meta:
        models=CompetitioninfoModel
        fields=["ID","MTUSER_ID","EMAIL","MODULE", "PIT_COMPT_HEADER","PIT_COMPT_BODY","PIT_COMPT_IMAGE","PIT_COMPT_VIDEO","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE"]