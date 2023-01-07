from rest_framework import serializers 
from MT_Startup_Pitch_Tractioninfo.models import TractioninfoModel
 
 
class TractioninfoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = TractioninfoModel
        fields = ("ID",
                  "MTUSER_ID",
                  "EMAIL",
                  "MODULE", 
                  "PIT_TRANS_HEADER",
                  "PIT_TRANS_BODY",
                  "PIT_TRANS_IMAGE",
                  "PIT_TRANS_VIDEO",
                  "STATUS",
                  "COMMENTS",
                  "DESCRIPTION",
                  "CREATED_USER",
                  "CREATED_DATE",
                  "MODIFIED_USER",
                  "MODIFIED_DATE")