from django.db import models
from django.forms import IntegerField

# Create your models here.
class InvestorsDetsModel(models.Model):
    MTUSER_ID = models.ForeignKey(to='self', on_delete=models.CASCADE)
    EMAIL=models.CharField(max_length=250)
    MODULE=models.CharField(max_length=50)
    INVESTOR_SNO=IntegerField
    INV_TEAM_NAME=models.CharField(max_length=150)
    TEAM_POSITION=models.CharField(max_length=250)
    FB_LINK=models.CharField(max_length=500)
    INSTA_LINK=models.CharField(max_length=500)
    LINKEDIN_LINK=models.CharField(max_length=500)
    BIO=models.CharField(max_length=500)
    PRO_PIC=models.BinaryField
    STATUS=models.CharField(max_length=50)
    COMMENTS=models.CharField(max_length=250)
    DESCRIPTION=models.CharField(max_length=250)
    CREATED_USER=models.CharField(max_length=150)
    CREATED_DATE=models.DateField()
    MODIFIED_USER=models.CharField(max_length=150)
    MODIFIED_DATE=models.DateField()
   
    
    def __str__(self):
        return self.title