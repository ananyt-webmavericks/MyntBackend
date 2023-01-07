from pydoc import classname
from django.contrib import admin

# Register your models here.
from .models import BusinfoModel

class Startup_Pitch_Businfo(admin.ModelAdmin):
         list_display= ("ID","MTUSER_ID","EMAIL","MODULE","PIT_BSMODEL_HEADER","PIT_BSMODEL_BODY","PIT_BSMODEL_IMAGE","PIT_BSMODEL_VIDEO","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE")

admin.site.register(BusinfoModel,Startup_Pitch_Businfo)