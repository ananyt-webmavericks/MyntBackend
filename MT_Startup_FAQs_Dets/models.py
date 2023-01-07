from tkinter.messagebox import QUESTION
from django.db import models
from django.forms import IntegerField

# Create your models here.
class FAQsModel(models.Model):
    MTUSER_ID = models.ForeignKey(to='self', on_delete=models.CASCADE)
    EMAIL=models.CharField(max_length=250)
    MODULE=models.CharField(max_length=50)
    FAQ_SNO=IntegerField
    QUESTION=models.CharField(max_length=500)
    ANSWER=models.CharField(max_length=900)
    STATUS=models.CharField(max_length=50)
    COMMENTS=models.CharField(max_length=250)
    DESCRIPTION=models.CharField(max_length=250)
    CREATED_USER=models.CharField(max_length=150)
    CREATED_DATE=models.DateField()
    MODIFIED_USER=models.CharField(max_length=150)
    MODIFIED_DATE=models.DateField()
   
    
    def __str__(self):
        return self.title