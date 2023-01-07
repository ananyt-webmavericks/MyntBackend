from dataclasses import fields
from django import forms
from django.contrib import forms

# Register your models here.
from .models import PaymentModel

class PaymentForm(forms.ModelAdmin):
    class meta:
        models=PaymentModel
        fields=["MTUSER_ID","EMAIL","MODULE","COMPANY_INVESTED_IN","INVESTED_DATE","INV_AMOUNT","INV_CONVENIENCE_FEE","INV_GST","INV_TOT","INV_CHK_AGREE_TERMS","INV_PAID","INV_BALANCE","AGREEMENT_FILE_DOC","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE"]