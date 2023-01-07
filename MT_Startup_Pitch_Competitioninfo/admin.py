from pydoc import classname
from django.contrib import admin

# Register your models here.
from .models import CompetitioninfoModel

class Startup_Pitch_Competitioninfo(admin.ModelAdmin):
         list_display= ("ID","MTUSER_ID","EMAIL","MODULE","PIT_COMPT_HEADER","PIT_COMPT_BODY","PIT_COMPT_IMAGE","PIT_COMPT_VIDEO","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE")

admin.site.register(CompetitioninfoModel,Startup_Pitch_Competitioninfo)