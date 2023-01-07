from rest_framework import serializers 
from MT_Startup_Pitch_Competitioninfo.models import CompetitioninfoModel
 
 
class CompetitioninfoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = CompetitioninfoModel
        fields = ("ID",
                  "MTUSER_ID",
                  "EMAIL",
                  "MODULE", 
                  "PIT_COMPT_HEADER",
                  "PIT_COMPT_BODY",
                  "PIT_COMPT_IMAGE",
                  "PIT_COMPT_VIDEO",
                  "STATUS",
                  "COMMENTS",
                  "DESCRIPTION",
                  "CREATED_USER",
                  "CREATED_DATE",
                  "MODIFIED_USER",
                  "MODIFIED_DATE")