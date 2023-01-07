from pydoc import classname
from django.contrib import admin

# Register your models here.
from .models import CamInvestorModel

class CampInvestor(admin.ModelAdmin):
         list_display= ("ID","MTUSER_ID","EMAIL","MODULE",
                        "CINV_SNO",
                        "CINV_MEMBER_NAME",
                        "CINV_MEMBER_POSITION",
                        "CINV_FB_LINK",
                        "CINV_INSTA_LINK",
                        "CINV_LINKEDIN_LINK",
                        "CINV_BIO",
                        "CINV_PROFILE_PIC",
                        "STATUS","COMMENTS",
                        "DESCRIPTION","CREATED_USER","CREATED_DATE",
                        "MODIFIED_USER","MODIFIED_DATE")

admin.site.register(CamInvestorModel,CampInvestor)