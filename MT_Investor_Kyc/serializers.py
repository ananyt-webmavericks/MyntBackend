from rest_framework import serializers 
from MT_Investor_Kyc.models import KycModel
 
 
class KycSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = KycModel
        fields = ("ID",
                  "MTUSER_ID",
                  "EMAIL",
                  "MODULE",
                  "INV_COUNTRYCODE",
                "INV_MOBILE_NUMBER",
                "INV_OTP",
                "INV_PAN",
                "INV_DOB",
                "INV_BANKACCNO",
                "INV_IFSCCODE",
                  "STATUS",
                  "COMMENTS",
                  "DESCRIPTION",
                  "CREATED_USER",
                  "CREATED_DATE",
                  "MODIFIED_USER",
                  "MODIFIED_DATE")