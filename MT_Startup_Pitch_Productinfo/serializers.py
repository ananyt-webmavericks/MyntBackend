from rest_framework import serializers
from MT_Startup_Pitch_Productinfo.models import ProductinfoModel
 
 
class ProductinfoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = ProductinfoModel
        fields = ("ID",
                  "MTUSER_ID",
                  "EMAIL",
                  "MODULE", 
                  "PIT_PROD_HEADER",
                  "PIT_PROD_BODY",
                  "PIT_PROD_IMAGE",
                  "PIT_PROD_VIDEO",
                  "STATUS",
                  "COMMENTS",
                  "DESCRIPTION",
                  "CREATED_USER",
                  "CREATED_DATE",
                  "MODIFIED_USER",
                  "MODIFIED_DATE")