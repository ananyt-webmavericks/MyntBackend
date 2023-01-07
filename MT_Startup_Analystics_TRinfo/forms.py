from dataclasses import fields
from django import forms
from django.contrib import forms

# Register your models here.
from .models import AnalysticsModel

class AnalysticsForm(forms.ModelAdmin):
    class meta:
        models=AnalysticsModel
        fields=["MTUSER_ID","EMAIL","MODULE","TR_ANAL_SNO","UPLOAD_IMAGES","TOTAL_REVENUE","GROWTH_PROFIT_MARGIN","MONTH_REC_REVENUE","CUS_CHURN_RATE","MONTHLY_ACTIVE_USERS","CAC_RATIO","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE"]