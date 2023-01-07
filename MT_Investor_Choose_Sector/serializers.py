from rest_framework import serializers 
from MT_Investor_Choose_Sector.models import Choose_SectorModel
 
 
class Choose_SectorSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Choose_SectorModel
        fields = ("ID",
                  "MTUSER_ID",
                  "EMAIL",
                  "MODULE",
                  "INV_CHOOSE_SECTOR",
                  "STATUS",
                  "COMMENTS",
                  "DESCRIPTION",
                  "CREATED_USER",
                  "CREATED_DATE",
                  "MODIFIED_USER",
                  "MODIFIED_DATE")