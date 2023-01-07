from pydoc import classname
from django.contrib import admin

# Register your models here.
from .models import VisioninfoModel

class Startup_Visioninfo(admin.ModelAdmin):
         list_display= ("ID","MTUSER_ID","EMAIL","MODULE","PIT_VSN_HEADER","PIT_VSN_BODY","PIT_VSN_IMAGE","PIT_VSN_VIDEO","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE")

admin.site.register(VisioninfoModel,Startup_Visioninfo)