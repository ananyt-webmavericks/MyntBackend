from pydoc import classname
from django.contrib import admin

# Register your models here.
from .models import CustomerinfoModel

class Startup_Pitch_Customerinfo(admin.ModelAdmin):
         list_display= ("ID","MTUSER_ID","EMAIL","MODULE","PIT_CUST_HEADER","PIT_CUST_BODY","PIT_CUST_IMAGE","PIT_CUST_VIDEO","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE")

admin.site.register(CustomerinfoModel,Startup_Pitch_Customerinfo)