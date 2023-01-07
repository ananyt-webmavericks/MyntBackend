from pydoc import classname
from django.contrib import admin

# Register your models here.
from .models import CampaignAnalyticsModel

class CampaignAnalytics(admin.ModelAdmin):
                  list_display= ("ID","MTUSER_ID","EMAIL","MODULE",
                         "ANLYSTICS_IMAGE",
      "ANLYSTICS_GROWTHPROFIT",
      "ANLYSTICS_MONRECURRING",
      "ANLYSTICS_CUSTCHURNRATE",
      "ANLYSTICS_MONACTIVEUSER",
      "ANLYSTICS_CACRATIO",
      "STATUS","COMMENTS",
      "DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE")

admin.site.register(CampaignAnalyticsModel,CampaignAnalytics)