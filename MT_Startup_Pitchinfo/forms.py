from dataclasses import fields
from django import forms
from django.contrib import forms

# Register your models here.
from .models import PitchinfoModel

class PitchinfoForm(forms.ModelAdmin):
    class meta:
        models=PitchinfoModel
        fields=["ID","MTUSER_ID","EMAIL","MODULE","PITCH_UPLOAD_DOC",
                "STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE",
                "MODIFIED_USER","MODIFIED_DATE"]