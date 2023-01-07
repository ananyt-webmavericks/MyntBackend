from dataclasses import fields
from django import forms
from django.contrib import forms

# Register your models here.
from .models import ProbleminfoModel

class ProbleminfoForm(forms.ModelAdmin):
    class meta:
        models=ProbleminfoModel
        fields=["ID","MTUSER_ID","EMAIL","MODULE",
                "CRT_PITCH_HEADER","CRT_PITCH_BODY","CRT_PITCH_IMAGE","CRT_PITCH_VIDEO",
                "STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE",
                "MODIFIED_USER","MODIFIED_DATE"]