from pydoc import classname
from django.contrib import admin

# Register your models here.
from .models import BannerModel

class Startup_Banner(admin.ModelAdmin):
         list_display= ("MTUSER_ID","EMAIL","MODULE","BANNER_SNO","BANNER_IMAGE","BANNER_VIDEO","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE")

admin.site.register(BannerModel,Startup_Banner)