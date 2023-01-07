from pydoc import classname
from django.contrib import admin

# Register your models here.
from .models import CampPressModel

class Campaign_PressAd(admin.ModelAdmin):
         list_display= ("ID","MTUSER_ID","EMAIL","MODULE",
                        "CAMP_PRESS_HEADER","CAMP_PRESS_BODY","CAMP_PRESS_IMAGE"
                        ,"CAMP_PRESS_VIDEO","STATUS","COMMENTS","DESCRIPTION",
                        "CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE")



admin.site.register(CampPressModel,Campaign_PressAd)
 