from rest_framework import serializers 
from MT_Startup_Agreements.models import AgreementsModel
 
 
class AgreementsSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = AgreementsModel
        fields = ("id",
                  "MTUSER_ID",
                  "EMAIL",
                  "MODULE",
                  "ESIGN_DOC",
                  "STATUS",
                  "COMMENTS",
                  "DESCRIPTION",
                  "CREATED_USER",
                  "CREATED_DATE",
                  "MODIFIED_USER",
                  "MODIFIED_DATE")