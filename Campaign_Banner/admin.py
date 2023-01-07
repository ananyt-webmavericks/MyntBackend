from pydoc import classname
from django.contrib import admin

# Register your models here.
from .models import CampaignBannerModel

class CampaignBanner(admin.ModelAdmin):
                  list_display= ("ID","MTUSER_ID","EMAIL","MODULE",
                         "CAM_BAN_IMAGE"
                        ,"CAM_BAN_VIDEO","STATUS","COMMENTS","DESCRIPTION",
                        "CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE")

admin.site.register(CampaignBannerModel,CampaignBanner)