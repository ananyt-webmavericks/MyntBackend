from rest_framework import serializers 
from MT_Startup_Pitch_Customerinfo.models import CustomerinfoModel
 
 
class CustomerinfoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = CustomerinfoModel
        fields = ("ID",
                  "MTUSER_ID",
                  "EMAIL",
                  "MODULE", 
                  "PIT_CUST_HEADER",
                  "PIT_CUST_BODY",
                  "PIT_CUST_IMAGE",
                  "PIT_CUST_VIDEO",
                  "STATUS",
                  "COMMENTS",
                  "DESCRIPTION",
                  "CREATED_USER",
                  "CREATED_DATE",
                  "MODIFIED_USER",
                  "MODIFIED_DATE")