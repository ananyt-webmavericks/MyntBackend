from pydoc import classname
from django.contrib import admin

# Register your models here.
from .models import TractioninfoModel

class Startup_Pitch_Tractioninfo(admin.ModelAdmin):
         list_display= ("ID","MTUSER_ID","EMAIL","MODULE","PIT_TRANS_HEADER","PIT_TRANS_BODY","PIT_TRANS_IMAGE","PIT_TRANS_VIDEO","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE")

admin.site.register(TractioninfoModel,Startup_Pitch_Tractioninfo)