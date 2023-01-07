from django.db import models

# Create your models here.
class StandardsModel(models.Model):
    ID = models.AutoField(primary_key=True)
    MTUSER_ID = models.CharField(max_length=250)
    EMAIL=models.CharField(max_length=250)
    MODULE=models.CharField(max_length=50)
    INV_RISK=models.CharField(max_length=25)
    INV_LIMITED_TRANSFER=models.CharField(max_length=25)
    INV_DIVERSIFICATION=models.CharField(max_length=25)
    INV_CANCELLATION=models.CharField(max_length=25)
    INV_RESEARCH=models.CharField(max_length=25)
    STATUS=models.CharField(max_length=50)
    COMMENTS=models.CharField(max_length=250)
    DESCRIPTION=models.CharField(max_length=250)
    CREATED_USER=models.CharField(max_length=150)
    CREATED_DATE=models.DateField()
    MODIFIED_USER=models.CharField(max_length=150)
    MODIFIED_DATE=models.DateField()