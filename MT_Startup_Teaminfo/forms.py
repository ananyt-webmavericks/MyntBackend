from dataclasses import fields
from django import forms
from django.contrib import forms

# Register your models here.
from .models import TeaminfoModel

class TeaminfoForm(forms.ModelAdmin):
    class meta:
        models=TeaminfoModel
        fields=["ID","MTUSER_ID","EMAIL","MODULE","TEAM_SNO","TEAM_MEMBER_NAME","TEAM_MEMBER_POSITION","FB_LINK","INSTA_LINK","LINKEDIN_LINK","TEAM_BIO","PROFILE_PIC","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE"]