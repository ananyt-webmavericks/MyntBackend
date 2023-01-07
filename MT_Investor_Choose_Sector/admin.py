from pydoc import classname
from django.contrib import admin

# Register your models here.
from .models import Choose_SectorModel

class Investor_Choose_Sector(admin.ModelAdmin):
         list_display= ("MTUSER_ID","EMAIL","MODULE",
                        "INV_CHOOSE_SECTOR","STATUS","COMMENTS",
                        "DESCRIPTION","CREATED_USER","CREATED_DATE",
                        "MODIFIED_USER","MODIFIED_DATE")

admin.site.register(Choose_SectorModel,Investor_Choose_Sector)