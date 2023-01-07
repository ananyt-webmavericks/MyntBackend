from pydoc import classname
from django.contrib import admin

# Register your models here.
from .models import SolutionModel

class Startup_Pitch_Solution(admin.ModelAdmin):
         list_display= ("ID","MTUSER_ID","EMAIL","MODULE",
                        "PIT_SOL_HEADER",
                        "PIT_SOL_BODY",
                        "PIT_SOL_IMAGE",
                        "PIT_SOL_VIDEO",
                        "STATUS","COMMENTS","DESCRIPTION","CREATED_USER","CREATED_DATE","MODIFIED_USER","MODIFIED_DATE")

admin.site.register(SolutionModel,Startup_Pitch_Solution)