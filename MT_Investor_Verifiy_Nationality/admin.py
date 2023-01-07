from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import NationalityModel


class Investor_Verify_Nationality(admin.ModelAdmin):
         list_display= ("MTUSER_ID","EMAIL","MODULE",
                        "NATIONALITY",
                        "STATUS","COMMENTS","DESCRIPTION",
                        "CREATED_USER","CREATED_DATE",
                        "MODIFIED_USER","MODIFIED_DATE")

admin.site.register(NationalityModel,Investor_Verify_Nationality)