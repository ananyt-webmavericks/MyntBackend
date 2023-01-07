# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import KycModel


class Investor_Kyc(admin.ModelAdmin):
         list_display= ("MTUSER_ID","EMAIL","MODULE",
                        "INV_COUNTRYCODE",
              "INV_MOBILE_NUMBER",
              "INV_OTP",
              "INV_PAN",
              "INV_DOB",
              "INV_BANKACCNO",
              "INV_IFSCCODE",
                        "STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE")

admin.site.register(KycModel,Investor_Kyc)