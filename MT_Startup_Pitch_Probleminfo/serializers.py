from rest_framework import serializers 
from MT_Startup_Pitch_Probleminfo.models import ProbleminfoModel
 
 
class ProbleminfoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = ProbleminfoModel
        fields = ("ID",
                  "MTUSER_ID",
                  "EMAIL",
                  "MODULE",
                  "CRT_PITCH_HEADER",
                  "CRT_PITCH_BODY",
                  "CRT_PITCH_IMAGE",
                  "CRT_PITCH_VIDEO", 
                  "STATUS",
                  "COMMENTS",
                  "DESCRIPTION",
                  "CREATED_USER",
                  "CREATED_DATE",
                  "MODIFIED_USER",
                  "MODIFIED_DATE")