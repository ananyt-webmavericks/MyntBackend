from rest_framework import serializers 
from MT_Startup_Teaminfo.models import TeaminfoModel
 
 
class TeaminfoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = TeaminfoModel
        fields = ( "ID",
                   "MTUSER_ID",
                    "EMAIL",
                    "MODULE",
                    "TEAM_SNO",
                    "TEAM_MEMBER_NAME",
                    "TEAM_MEMBER_POSITION",
                    "FB_LINK",
                    "INSTA_LINK",
                    "LINKEDIN_LINK",
                    "TEAM_BIO",
                    "PROFILE_PIC",
                    "STATUS",
                    "COMMENTS",
                    "DESCRIPTION",
                    "CREATED_USER",
                    "CREATED_DATE",
                    "MODIFIED_USER",
                    "MODIFIED_DATE")