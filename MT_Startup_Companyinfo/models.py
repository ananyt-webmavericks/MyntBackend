from tkinter import DoubleVar
from django.db import models

# Create your models here.
class CompanyinfoModel(models.Model):
    ID = models.AutoField(primary_key=True)
    MTUSER_ID = models.CharField(max_length=250)
    EMAIL=models.CharField(max_length=250)
    MODULE=models.CharField(max_length=50)
    COUNTRY=models.CharField(max_length=150)
    STATE=models.CharField(max_length=150)
    CITY=models.CharField(max_length=75)
    PINCODE=models.CharField(max_length=50)
    ADDRESS=models.CharField(max_length=500)
    COMPANY_WEBSITE=models.CharField(max_length=250)
    FB_LINK=models.CharField(max_length=500)
    INSTA_LINK=models.CharField(max_length=500)
    LINKEDIN_LINK=models.CharField(max_length=500)
    LEGAL_NAME=models.CharField(max_length=250)
    CIN_NUMBER=models.CharField(max_length=250)
    DATE_OF_INCORPORATATION=models.DateField()
    INCORPORATION_TYPE=models.CharField(max_length=500)
    ABOUT_COMPANY=models.CharField(max_length=500)
    AMOUNT_INVESTED=models.CharField(max_length=500)
    NO_OF_EMPLOYEES=models.CharField(max_length=150)
    STATUS=models.CharField(max_length=50)
    COMMENTS=models.CharField(max_length=250)
    DESCRIPTION=models.CharField(max_length=250)
    CREATED_USER=models.CharField(max_length=150)
    CREATED_DATE=models.DateField()
    MODIFIED_USER=models.CharField(max_length=150)
    MODIFIED_DATE=models.DateField()
   