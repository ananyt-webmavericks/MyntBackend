from rest_framework import serializers 
from Campaign_Banner.models import CampaignBannerModel
 
 
class CampaignBannerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = CampaignBannerModel
        fields = ("ID",
                  "MTUSER_ID",
                  "EMAIL",
                  "MODULE", 
                  "CAM_BAN_IMAGE",
                  "CAM_BAN_VIDEO", 
                  "STATUS",
                  "COMMENTS",
                  "DESCRIPTION",
                  "CREATED_USER",
                  "CREATED_DATE",
                  "MODIFIED_USER",
                  "MODIFIED_DATE")