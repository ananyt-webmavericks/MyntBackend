from rest_framework import serializers 
from MT_Startup_Pitch_Usagefundsinfo.models import UsagefundsinfoModel
 
 
class UsagefundsinfoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = UsagefundsinfoModel
        fields = ("ID",
                  "MTUSER_ID",
                  "EMAIL",
                  "MODULE", 
                  "PIT_USAGE_HEADER",
                  "PIT_USAGE_BODY",
                  "PIT_USAGE_IMAGE",
                  "PIT_USAGE_VIDEO",
                  "STATUS",
                  "COMMENTS",
                  "DESCRIPTION",
                  "CREATED_USER",
                  "CREATED_DATE",
                  "MODIFIED_USER",
                  "MODIFIED_DATE")