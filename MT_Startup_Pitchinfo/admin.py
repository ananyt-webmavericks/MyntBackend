from pydoc import classname
from django.contrib import admin

# Register your models here.
from .models import PitchinfoModel

class Startup_Pitchinfo(admin.ModelAdmin):
         list_display= ("MTUSER_ID",
                        "EMAIL",
                        "MODULE",
                        "PITCH_UPLOAD_DOC", 
                        "STATUS",
                        "COMMENTS",
                        "DESCRIPTION",
                        "CREATED_USER",
                        "CREATED_DATE",
                        "MODIFIED_USER",
                        "MODIFIED_DATE")

admin.site.register(PitchinfoModel,Startup_Pitchinfo)