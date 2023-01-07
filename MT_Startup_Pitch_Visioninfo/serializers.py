from rest_framework import serializers 
from MT_Startup_Pitch_Visioninfo.models import VisioninfoModel
 
 
class VisioninfoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = VisioninfoModel
        fields = ("ID",
                  "MTUSER_ID",
                  "EMAIL",
                  "MODULE", 
                  "PIT_VSN_HEADER",
                  "PIT_VSN_BODY",
                  "PIT_VSN_IMAGE",
                  "PIT_VSN_VIDEO",
                  "STATUS",
                  "COMMENTS",
                  "DESCRIPTION",
                  "CREATED_USER",
                  "CREATED_DATE",
                  "MODIFIED_USER",
                  "MODIFIED_DATE")