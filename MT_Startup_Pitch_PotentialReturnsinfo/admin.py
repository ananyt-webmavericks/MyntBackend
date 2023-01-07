from pydoc import classname
from django.contrib import admin

# Register your models here.
from .models import PotentialReturnsinfoModel

class Startup_Pitch_PotentialReturnsinfo(admin.ModelAdmin):
         list_display= ("ID","MTUSER_ID","EMAIL","MODULE","PIT_POTRET_HEADER","PIT_POTRET_BODY","PIT_POTRET_IMAGE","PIT_POTRET_VIDEO","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE")

admin.site.register(PotentialReturnsinfoModel,Startup_Pitch_PotentialReturnsinfo)