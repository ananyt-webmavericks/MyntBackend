from rest_framework import serializers 
from E_sign.models import E_SignModel
 
 
class ESignSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = E_SignModel
        fields = (  "ID", 
                    "ESIGN_UPLOAD_DOC",
                    "STATUS",
                    "COMMENTS",
                    "DESCRIPTION",
                    "CREATED_USER",
                    "CREATED_DATE",
                    "MODIFIED_USER",
                    "MODIFIED_DATE")