# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import PaymentModel


class Investor_Payment(admin.ModelAdmin):
         list_display= ("MTUSER_ID","EMAIL","MODULE","COMPANY_INVESTED_IN","INVESTED_DATE","INV_AMOUNT","INV_CONVENIENCE_FEE","INV_GST","INV_TOT","INV_CHK_AGREE_TERMS","INV_PAID","INV_BALANCE","AGREEMENT_FILE_DOC","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE")

admin.site.register(PaymentModel,Investor_Payment)