from pydoc import classname
from django.contrib import admin

# Register your models here.
from .models import ProductinfoModel

class Startup_Pitch_Productinfo(admin.ModelAdmin):
         list_display= ("ID","MTUSER_ID","EMAIL","MODULE", "PIT_PROD_HEADER","PIT_PROD_BODY","PIT_PROD_IMAGE","PIT_PROD_VIDEO","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE")

admin.site.register(ProductinfoModel,Startup_Pitch_Productinfo)