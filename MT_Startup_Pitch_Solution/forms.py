from dataclasses import fields
from django import forms
from django.contrib import forms

# Register your models here.
from .models import SolutionModel

class SolutionForm(forms.ModelAdmin):
    class meta:
        models= SolutionModel
        fields=["ID","MTUSER_ID","EMAIL","MODULE",
                "PIT_SOL_HEADER",
                        "PIT_SOL_BODY",
                        "PIT_SOL_IMAGE",
                        "PIT_SOL_VIDEO","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE"]