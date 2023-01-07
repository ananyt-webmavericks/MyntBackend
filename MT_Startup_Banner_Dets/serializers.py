from rest_framework import serializers 
from MT_Startup_Banner_Dets.models import BannerModel
 
 
class BannerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = BannerModel
        fields = ("id",
                  "MTUSER_ID",
                  "EMAIL",
                  "MODULE",
                  "BANNER_SNO",
                  "BANNER_IMAGE",
                  "BANNER_VIDEO",
                  "STATUS",
                  "COMMENTS",
                  "DESCRIPTION",
                  "CREATED_USER",
                  "CREATED_DATE",
                  "MODIFIED_USER",
                  "MODIFIED_DATE")