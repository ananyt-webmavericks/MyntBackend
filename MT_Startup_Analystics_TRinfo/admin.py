from pydoc import classname
from django.contrib import admin

# Register your models here.
from .models import AnalysticsModel

class Startup_Analystics_TRinfo(admin.ModelAdmin):
         list_display= ("MTUSER_ID","EMAIL","MODULE","TR_ANAL_SNO","UPLOAD_IMAGES","TOTAL_REVENUE","GROWTH_PROFIT_MARGIN","MONTH_REC_REVENUE","CUS_CHURN_RATE","MONTHLY_ACTIVE_USERS","CAC_RATIO","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE")

admin.site.register(AnalysticsModel,Startup_Analystics_TRinfo)