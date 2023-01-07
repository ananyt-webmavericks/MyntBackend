
from django.db import models

# Create your models here.

class SignupModel(models.Model):
    id = models.AutoField(primary_key=True)
    FIRSTNAME=models.CharField(max_length=150)
    LASTNAME=models.CharField(max_length=150)
    EMAIL=models.CharField(max_length=250)
    SCHOOL=models.CharField(max_length=500)
    PASSWORD=models.CharField(max_length=6)
    CONPASSWORD=models.CharField(max_length=6)
    ROLE=models.CharField(max_length=50)
    MODULE=models.CharField(max_length=50)
    AGREECHK=models.CharField(max_length=1)
    STATUS=models.CharField(max_length=50)
    COMMENTS=models.CharField(max_length=250)
    DESCRIPTION=models.CharField(max_length=250)
    CREATED_USER=models.CharField(max_length=150)
    CREATED_DATE=models.DateField()
    MODIFIED_USER=models.CharField(max_length=150)
    MODIFIED_DATE=models.DateField()
     

