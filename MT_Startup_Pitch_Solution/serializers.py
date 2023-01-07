from rest_framework import serializers
from MT_Startup_Pitch_Solution.models import SolutionModel
 
 
class SolutionSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = SolutionModel
        fields = ("ID",
                  "MTUSER_ID",
                  "EMAIL",
                  "MODULE",
                  "PIT_SOL_HEADER",
                  "PIT_SOL_BODY",
                  "PIT_SOL_IMAGE",
                  "PIT_SOL_VIDEO",
                  "STATUS",
                  "COMMENTS",
                  "DESCRIPTION",
                  "CREATED_USER",
                  "CREATED_DATE",
                  "MODIFIED_USER",
                  "MODIFIED_DATE")