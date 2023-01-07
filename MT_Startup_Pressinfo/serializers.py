from rest_framework import serializers 
from MT_Startup_Pressinfo.models import PressinfoModel
 
 
class PressinfoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = PressinfoModel
        fields = ("id",
                  "MTUSER_ID",
                  "EMAIL",
                  "MODULE",
                  "PRESS_SNO",
                  "PRESS_HEADER",
                  "PRESS_BODY",
                  "PRESS_IMAGE",
                  "PRESS_VIDEO",
                  "STATUS",
                  "COMMENTS",
                  "DESCRIPTION",
                  "CREATED_USER",
                  "CREATED_DATE",
                  "MODIFIED_USER",
                  "MODIFIED_DATE")