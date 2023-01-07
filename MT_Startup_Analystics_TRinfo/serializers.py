from rest_framework import serializers 
from MT_Startup_Analystics_TRinfo.models import AnalysticsModel
 
 
class AnalysticsSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = AnalysticsModel
        fields = ("id",
                  "MTUSER_ID",
                  "EMAIL",
                  "MODULE",
                  "TR_ANAL_SNO",
                  "UPLOAD_IMAGES",
                  "TOTAL_REVENUE",
                  "GROWTH_PROFIT_MARGIN",
                  "MONTH_REC_REVENUE",
                  "CUS_CHURN_RATE",
                  "MONTHLY_ACTIVE_USERS",
                  "CAC_RATIO",
                  "STATUS",
                  "COMMENTS",
                  "DESCRIPTION",
                  "CREATED_USER",
                  "CREATED_DATE",
                  "MODIFIED_USER",
                  "MODIFIED_DATE")