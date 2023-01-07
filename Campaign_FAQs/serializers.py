from rest_framework import serializers 
from Campaign_FAQs.models import CamFAQsModel
 
 
class CamFAQsSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = CamFAQsModel
        fields = ( "ID",
                   "MTUSER_ID",
                    "EMAIL",
                    "MODULE",
                    "CFAQ_SNO",
                    "CFAQ_QUESTION", 
                    "CFAQ_QANSWER",
                    "STATUS",
                    "COMMENTS",
                    "DESCRIPTION",
                    "CREATED_USER",
                    "CREATED_DATE",
                    "MODIFIED_USER",
                    "MODIFIED_DATE")