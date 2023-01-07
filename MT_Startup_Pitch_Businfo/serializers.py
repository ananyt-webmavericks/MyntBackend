from rest_framework import serializers 
from MT_Startup_Pitch_Businfo.models import BusinfoModel
 
 
class BusinfoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = BusinfoModel
        fields = ("ID",
                  "MTUSER_ID",
                  "EMAIL",
                  "MODULE", 
                  "PIT_BSMODEL_HEADER",
                  "PIT_BSMODEL_BODY",
                  "PIT_BSMODEL_IMAGE",
                  "PIT_BSMODEL_VIDEO",
                  "STATUS",
                  "COMMENTS",
                  "DESCRIPTION",
                  "CREATED_USER",
                  "CREATED_DATE",
                  "MODIFIED_USER",
                  "MODIFIED_DATE")