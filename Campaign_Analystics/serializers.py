from rest_framework import serializers 
from Campaign_Analystics.models import CampaignAnalyticsModel
 
 
class CamAnalyticsSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = CampaignAnalyticsModel
        fields = ( "ID",
                   "MTUSER_ID",
                    "EMAIL",
                    "MODULE",
                    "ANLYSTICS_IMAGE",
                    "ANLYSTICS_GROWTHPROFIT",
                    "ANLYSTICS_MONRECURRING",
                    "ANLYSTICS_CUSTCHURNRATE",
                    "ANLYSTICS_MONACTIVEUSER",
                    "ANLYSTICS_CACRATIO", 
                    "STATUS",
                    "COMMENTS",
                    "DESCRIPTION",
                    "CREATED_USER",
                    "CREATED_DATE",
                    "MODIFIED_USER",
                    "MODIFIED_DATE")