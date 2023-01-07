from django.db import models

# Create your models here.
class PressinfoModel(models.Model):
    MTUSER_ID = models.ForeignKey(to='self', on_delete=models.CASCADE)
    EMAIL=models.CharField(max_length=250)
    MODULE=models.CharField(max_length=50) 
    PRESS_SNO=models.CharField(max_length=150)
    PRESS_HEADER=models.CharField(max_length=500)
    PRESS_BODY=models.CharField(max_length=500)
    PRESS_IMAGE=models.BinaryField
    PRESS_VIDEO=models.BigAutoField
    STATUS=models.CharField(max_length=50)
    COMMENTS=models.CharField(max_length=250)
    DESCRIPTION=models.CharField(max_length=250)
    CREATED_USER=models.CharField(max_length=150)
    CREATED_DATE=models.DateField()
    MODIFIED_USER=models.CharField(max_length=150)
    MODIFIED_DATE=models.DateField()
   
    
    def __str__(self):
        return self.title