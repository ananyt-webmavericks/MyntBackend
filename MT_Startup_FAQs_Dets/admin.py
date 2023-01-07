from pydoc import classname
from django.contrib import admin

# Register your models here.
from .models import FAQsModel

class Startup_FAQs_Dets(admin.ModelAdmin):
         list_display= ("MTUSER_ID","EMAIL","MODULE","FAQ_SNO","QUESTION","ANSWER","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE")

admin.site.register(FAQsModel,Startup_FAQs_Dets)
