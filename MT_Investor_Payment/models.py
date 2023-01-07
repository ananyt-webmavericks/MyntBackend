from tkinter import DoubleVar
from MySQLdb import Date
from django.db import models
from django.forms import DateField, FloatField, IntegerField

# Create your models here.
class PaymentModel(models.Model):
    MTUSER_ID = models.ForeignKey(to='self', on_delete=models.CASCADE)
    EMAIL=models.CharField(max_length=250)
    MODULE=models.CharField(max_length=50)
    COMPANY_INVESTED_IN=models.CharField(max_length=50)
    INVESTED_DATE=DateField
    INV_AMOUNT=DoubleVar
    INV_CONVENIENCE_FEE=DoubleVar
    INV_GST=FloatField
    INV_TOT=DoubleVar
    INV_CHK_AGREE_TERMS=DoubleVar
    INV_PAID=DoubleVar
    INV_BALANCE=DoubleVar
    AGREEMENT_FILE_DOC=models.BinaryField()
    STATUS=models.CharField(max_length=50)
    COMMENTS=models.CharField(max_length=250)
    DESCRIPTION=models.CharField(max_length=250)
    CREATED_USER=models.CharField(max_length=150)
    CREATED_DATE=models.DateField()
    MODIFIED_USER=models.CharField(max_length=150)
    MODIFIED_DATE=models.DateField()
   
    
    def __str__(self):
        return self.title