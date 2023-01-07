from tkinter import DoubleVar
from django.db import models
from django.forms import FloatField, IntegerField

# Create your models here.
class AnalysticsModel(models.Model):
    MTUSER_ID = models.ForeignKey(to='self', on_delete=models.CASCADE)
    EMAIL=models.CharField(max_length=250)
    MODULE=models.CharField(max_length=50)
    TR_ANAL_SNO=IntegerField
    UPLOAD_IMAGES=models.BinaryField
    TOTAL_REVENUE=DoubleVar
    GROWTH_PROFIT_MARGIN=FloatField
    MONTH_REC_REVENUE=DoubleVar
    CUS_CHURN_RATE=FloatField
    MONTHLY_ACTIVE_USERS=DoubleVar
    CAC_RATIO=FloatField
    STATUS=models.CharField(max_length=50)
    COMMENTS=models.CharField(max_length=250)
    DESCRIPTION=models.CharField(max_length=250)
    CREATED_USER=models.CharField(max_length=150)
    CREATED_DATE=models.DateField()
    MODIFIED_USER=models.CharField(max_length=150)
    MODIFIED_DATE=models.DateField()
   
    
    def __str__(self):
        return self.title