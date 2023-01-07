from pydoc import classname
from django.contrib import admin

# Register your models here.
from .models import TeaminfoModel

class Startup_Teaminfo(admin.ModelAdmin):
         list_display= ("MTUSER_ID","EMAIL","MODULE","TEAM_SNO","TEAM_MEMBER_NAME","TEAM_MEMBER_POSITION","FB_LINK","INSTA_LINK","LINKEDIN_LINK","TEAM_BIO","PROFILE_PIC","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE")

admin.site.register(TeaminfoModel,Startup_Teaminfo)