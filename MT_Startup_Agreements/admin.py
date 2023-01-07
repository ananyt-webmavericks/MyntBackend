from pydoc import classname
from django.contrib import admin

# Register your models here.
from .models import AgreementsModel

class Startup_Agreements(admin.ModelAdmin):
         list_display= ("MTUSER_ID","EMAIL","MODULE","ESIGN_DOC","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE")

admin.site.register(AgreementsModel,Startup_Agreements)