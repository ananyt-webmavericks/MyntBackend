from rest_framework import serializers 
from MT_Investor_Verify_Standards.models import StandardsModel
 
 
class StandardsSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = StandardsModel
        fields = ("ID",
                  "MTUSER_ID",
                  "EMAIL",
                  "MODULE",
                  "INV_RISK",
                  "INV_LIMITED_TRANSFER",
                  "INV_DIVERSIFICATION",
                  "INV_CANCELLATION",
                  "INV_RESEARCH",
                  "STATUS",
                  "COMMENTS",
                  "DESCRIPTION",
                  "CREATED_USER",
                  "CREATED_DATE",
                  "MODIFIED_USER",
                  "MODIFIED_DATE")