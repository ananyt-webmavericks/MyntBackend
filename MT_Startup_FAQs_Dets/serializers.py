from rest_framework import serializers 
from MT_Startup_FAQs_Dets.models import FAQsModel
 
 
class FAQsSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = FAQsModel
        fields = ("id",
                  "MTUSER_ID",
                  "EMAIL",
                  "MODULE",
                  "FAQ_SNO",
                  "QUESTION",
                  "ANSWER",
                  "STATUS",
                  "COMMENTS",
                  "DESCRIPTION",
                  "CREATED_USER",
                  "CREATED_DATE",
                  "MODIFIED_USER",
                  "MODIFIED_DATE")