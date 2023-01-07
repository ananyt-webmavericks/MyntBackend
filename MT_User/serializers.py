from rest_framework import serializers 
from MT_User.models import SignupModel
 
 
class SignupSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = SignupModel
        fields = (  'id',
                    'FIRSTNAME' ,
                    'LASTNAME',
                    'EMAIL',
                    'SCHOOL',
                    'PASSWORD',
                    'CONPASSWORD',
                    'ROLE' ,
                    'MODULE',
                    'AGREECHK',
                    'STATUS',
                    'COMMENTS',
                    'DESCRIPTION',
                    'CREATED_USER',
                    'CREATED_DATE',
                    'MODIFIED_USER',
                    'MODIFIED_DATE')