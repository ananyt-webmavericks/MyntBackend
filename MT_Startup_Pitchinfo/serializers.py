from rest_framework import serializers 
from MT_Startup_Pitchinfo.models import PitchinfoModel
 
 
class PitchinfoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = PitchinfoModel
        fields = ("ID",
                  "MTUSER_ID",
                  "EMAIL",
                  "MODULE",
                  "PITCH_UPLOAD_DOC", 
                  "STATUS",
                  "COMMENTS",
                  "DESCRIPTION",
                  "CREATED_USER",
                  "CREATED_DATE",
                  "MODIFIED_USER",
                  "MODIFIED_DATE")