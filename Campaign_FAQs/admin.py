from pydoc import classname
from django.contrib import admin

# Register your models here.
from .models import CamFAQsModel

class CamFAQs(admin.ModelAdmin):
         list_display= ("ID","MTUSER_ID","EMAIL","MODULE",
                        "CFAQ_SNO",
                        "CFAQ_QUESTION", 
                        "CFAQ_QANSWER", 
                        "STATUS","COMMENTS",
                        "DESCRIPTION","CREATED_USER","CREATED_DATE",
                        "MODIFIED_USER","MODIFIED_DATE")

admin.site.register(CamFAQsModel,CamFAQs)