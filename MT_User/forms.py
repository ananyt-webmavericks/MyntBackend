from dataclasses import fields
from django import forms


# Register your models here.
from .models import SignupModel

class SignupForm(forms.ModelForm):
    class meta:
        models=SignupModel
        fields=["id","FIRSTNAME","LASTNAME","EMAIL","SCHOOL","PASSWORD","CONPASSWORD","ROLE","MODULE","AGREECHK","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE"]