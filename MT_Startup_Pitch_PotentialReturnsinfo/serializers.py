from rest_framework import serializers 
from MT_Startup_Pitch_PotentialReturnsinfo.models import PotentialReturnsinfoModel
 
 
class PotentialReturnsinfoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = PotentialReturnsinfoModel
        fields = ("ID",
                  "MTUSER_ID",
                  "EMAIL",
                  "MODULE", 
                  "PIT_POTRET_HEADER",
                  "PIT_POTRET_BODY",
                  "PIT_POTRET_IMAGE",
                  "PIT_POTRET_VIDEO",
                  "STATUS",
                  "COMMENTS",
                  "DESCRIPTION",
                  "CREATED_USER",
                  "CREATED_DATE",
                  "MODIFIED_USER",
                  "MODIFIED_DATE")