from pydoc import classname
from django.contrib import admin

# Register your models here.
from .models import E_SignModel

class E_Sign(admin.ModelAdmin):
         list_display= ("ID",  
      "ESIGN_UPLOAD_DOC",
      "STATUS",
      "COMMENTS",
      "DESCRIPTION",
      "CREATED_USER",
      "CREATED_DATE",
      "MODIFIED_USER",
      "MODIFIED_DATE" )

admin.site.register(E_SignModel,E_Sign)