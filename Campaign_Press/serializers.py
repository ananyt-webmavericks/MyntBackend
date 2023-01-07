from rest_framework import serializers 
from Campaign_Press.models import CampPressModel
 
 
class CampaignPressSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = CampPressModel
        fields = ("ID",
                  "MTUSER_ID",
                  "EMAIL",
                  "MODULE",
                  "CAMP_PRESS_HEADER",
                  "CAMP_PRESS_BODY",
                  "CAMP_PRESS_IMAGE",
                  "CAMP_PRESS_VIDEO", 
                  "STATUS",
                  "COMMENTS",
                  "DESCRIPTION",
                  "CREATED_USER",
                  "CREATED_DATE",
                  "MODIFIED_USER",
                  "MODIFIED_DATE")