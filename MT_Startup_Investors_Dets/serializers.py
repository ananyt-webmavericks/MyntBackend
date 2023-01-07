from rest_framework import serializers 
from MT_Startup_Investors_Dets.models import InvestorsDetsModel
 
 
class InvestorsDetsSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = InvestorsDetsModel
        fields = ("id",
                  "MTUSER_ID",
                  "EMAIL",
                  "MODULE",
                  "INVESTOR_SNO",
                  "INV_TEAM_NAME",
                  "TEAM_POSITION",
                  "FB_LINK",
                  "INSTA_LINK",
                  "LINKEDIN_LINK",
                  "BIO",
                  "PRO_PIC",
                  "STATUS",
                  "COMMENTS",
                  "DESCRIPTION",
                  "CREATED_USER",
                  "CREATED_DATE",
                  "MODIFIED_USER",
                  "MODIFIED_DATE")