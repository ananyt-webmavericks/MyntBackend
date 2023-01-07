from pydoc import classname
from django.contrib import admin

# Register your models here.
from .models import PressinfoModel

class Startup_Pressinfo(admin.ModelAdmin):
         list_display= ("MTUSER_ID","EMAIL","MODULE","PRESS_SNO","PRESS_HEADER","PRESS_BODY","PRESS_IMAGE","PRESS_VIDEO","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE")

admin.site.register(PressinfoModel,Startup_Pressinfo)