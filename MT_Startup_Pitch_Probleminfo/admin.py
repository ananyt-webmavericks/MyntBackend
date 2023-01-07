from pydoc import classname
from django.contrib import admin

# Register your models here.
from .models import ProbleminfoModel

class Startup_Pitch_Probleminfo(admin.ModelAdmin):
         list_display= ("ID","MTUSER_ID","EMAIL","MODULE",
                        "CRT_PITCH_HEADER","CRT_PITCH_BODY","CRT_PITCH_IMAGE"
                        ,"CRT_PITCH_VIDEO","STATUS","COMMENTS","DESCRIPTION",
                        "CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE")

admin.site.register(ProbleminfoModel,Startup_Pitch_Probleminfo)