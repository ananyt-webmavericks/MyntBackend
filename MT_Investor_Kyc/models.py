from django.db import models
from django.forms import IntegerField

# Create your models here.
class KycModel(models.Model):
    ID = models.AutoField(primary_key=True)
    MTUSER_ID = models.CharField(max_length=250)
    EMAIL=models.CharField(max_length=250)
    MODULE=models.CharField(max_length=50)
    INV_COUNTRYCODE=models.CharField(max_length=50)
    INV_MOBILE_NUMBER=models.CharField(max_length=50)
    INV_OTP=models.CharField(max_length=50)
    INV_PAN=models.CharField(max_length=50)
    INV_DOB=models.CharField(max_length=50)
    INV_BANKACCNO=models.CharField(max_length=50)
    INV_IFSCCODE=models.CharField(max_length=50) 
    STATUS=models.CharField(max_length=50)
    COMMENTS=models.CharField(max_length=250)
    DESCRIPTION=models.CharField(max_length=250)
    CREATED_USER=models.CharField(max_length=150)
    CREATED_DATE=models.DateField()
    MODIFIED_USER=models.CharField(max_length=150)
    MODIFIED_DATE=models.DateField()
   
    