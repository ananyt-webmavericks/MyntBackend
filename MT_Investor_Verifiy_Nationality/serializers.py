from rest_framework import serializers 
from MT_Investor_Verifiy_Nationality.models import NationalityModel
 
 
class NationalitySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = NationalityModel
        fields = ( "ID",
                    "MTUSER_ID",
                    "EMAIL",
                    "MODULE",
                    "NATIONALITY",
                    "STATUS",
                    "COMMENTS",
                    "DESCRIPTION",
                    "CREATED_USER",
                    "CREATED_DATE",
                    "MODIFIED_USER",
                    "MODIFIED_DATE")