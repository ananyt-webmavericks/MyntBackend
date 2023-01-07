from pydoc import classname
from django.contrib import admin

# Register your models here.
from .models import InvestorsDetsModel

class Startup_Investors_Dets(admin.ModelAdmin):
         list_display= ("MTUSER_ID","EMAIL","MODULE","INVESTOR_SNO","INV_TEAM_NAME","TEAM_POSITION","FB_LINK","INSTA_LINK","LINKEDIN_LINK","BIO","PRO_PIC","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE")

admin.site.register(InvestorsDetsModel,Startup_Investors_Dets)