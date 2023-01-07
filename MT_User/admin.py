from pydoc import classname
from django.contrib import admin

# Register your models here.
from .models import SignupModel

class MT_UserAdmin(admin.ModelAdmin):
         list_display= ("id","FIRSTNAME","LASTNAME","EMAIL","SCHOOL","PASSWORD","CONPASSWORD","ROLE","MODULE","AGREECHK","STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE")

admin.site.register(SignupModel,MT_UserAdmin)
