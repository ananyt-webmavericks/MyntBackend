from pydoc import classname
from django.contrib import admin

# Register your models here.
from .models import RaiseModel

class Startup_Raise(admin.ModelAdmin):
         list_display= ("MTUSER_ID",
      "EMAIL",
      "MODULE",
      "RAISE_NAME",
      "RAISE_EMAIL",
      "RAISE_FOUNDER_URL1",
      "RAISE_FOUNDER_URL2",
      "RAISE_COMPANY_NAME",
      "RAISE_COM_LINKPAGE",
      "RAISE_WEBSITE",
      "RAISE_FUNDRAISING",
      "RAISE_PROD_DESC",
      "RAISE_TRACTION",
      "RAISE_REVENUE",
      "RAISE_TEAM",
      "RAISE_COMROUND",
      "RAISE_MTRIGHTS",
      "RAISE_EXIST_COM",
      "RAISE_PRIVATEROUND",
      "RAISE_UPLOAD_DOC",
      "STATUS",
      "COMMENTS",
      "DESCRIPTION",
      "CREATED_USER",
      "CREATED_DATE",
      "MODIFIED_USER",
      "MODIFIED_DATE" )

admin.site.register(RaiseModel,Startup_Raise)