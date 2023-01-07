from pydoc import classname
from django.contrib import admin

# Register your models here.
from .models import StandardsModel

class Investor_Verify_Standards(admin.ModelAdmin):
         list_display= ("MTUSER_ID","EMAIL","MODULE",
                        "INV_RISK","INV_LIMITED_TRANSFER",
                        "INV_DIVERSIFICATION","INV_CANCELLATION",
                        "INV_RESEARCH","STATUS","COMMENTS",
                        "DESCRIPTION","CREATED_USER","CREATED_DATE",
                        "MODIFIED_USER","MODIFIED_DATE")

admin.site.register(StandardsModel,Investor_Verify_Standards)