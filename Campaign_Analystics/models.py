from django.db import models

# lets us explicitly set upload path and filename
def upload_imgto(instance, filename):
    return 'images/campaign_analytics/{filename}'.format(filename=filename)
 
# Create your models here.
class CampaignAnalyticsModel(models.Model):
    ID = models.AutoField(primary_key=True)
    MTUSER_ID = models.CharField(max_length=250)
    EMAIL=models.CharField(max_length=250)
    MODULE=models.CharField(max_length=50) 
    ANLYSTICS_IMAGE =models.ImageField(upload_to=upload_imgto, blank=True, null=True)
    ANLYSTICS_GROWTHPROFIT=models.CharField(max_length=50)
    ANLYSTICS_MONRECURRING=models.CharField(max_length=50) 
    ANLYSTICS_CUSTCHURNRATE=models.CharField(max_length=50)
    ANLYSTICS_MONACTIVEUSER=models.CharField(max_length=50)
    ANLYSTICS_CACRATIO=models.CharField(max_length=50)
    STATUS=models.CharField(max_length=50)
    COMMENTS=models.CharField(max_length=250)
    DESCRIPTION=models.CharField(max_length=250)
    CREATED_USER=models.CharField(max_length=150)
    CREATED_DATE=models.DateField()
    MODIFIED_USER=models.CharField(max_length=150)
    MODIFIED_DATE=models.DateField() 