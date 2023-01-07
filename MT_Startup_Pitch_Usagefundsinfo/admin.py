from pydoc import classname
from django.contrib import admin

# Register your models here.
from .models import UsagefundsinfoModel

class Startup_Pitch_Usagefundsinfo(admin.ModelAdmin):
         list_display= ("ID","MTUSER_ID","EMAIL","MODULE","PIT_USAGE_HEADER","PIT_USAGE_BODY","PIT_USAGE_IMAGE","PIT_USAGE_VIDEO","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE")

admin.site.register(UsagefundsinfoModel,Startup_Pitch_Usagefundsinfo)