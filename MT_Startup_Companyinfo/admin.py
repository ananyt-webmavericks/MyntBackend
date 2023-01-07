from pydoc import classname
from django.contrib import admin

# Register your models here.
from .models import CompanyinfoModel

class Startup_Companyinfo(admin.ModelAdmin):
         list_display= ("MTUSER_ID","EMAIL","MODULE","COUNTRY","STATE","CITY","PINCODE","ADDRESS","COMPANY_WEBSITE","FB_LINK","INSTA_LINK","LINKEDIN_LINK","LEGAL_NAME","CIN_NUMBER","DATE_OF_INCORPORATATION","INCORPORATION_TYPE","ABOUT_COMPANY","AMOUNT_INVESTED","NO_OF_EMPLOYEES","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE")

admin.site.register(CompanyinfoModel,Startup_Companyinfo)