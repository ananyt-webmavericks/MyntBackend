from django.db import models

# lets us explicitly set upload path and filename
def upload_imgto(instance, filename):
    return 'images/pitch_solution/{filename}'.format(filename=filename)

# lets us explicitly set upload path and filename
def upload_vidto(instance, filename):
    return 'videos/pitch_solution/{filename}'.format(filename=filename)
# Create your models here.
class SolutionModel(models.Model):
    ID = models.AutoField(primary_key=True)
    MTUSER_ID = models.CharField(max_length=250)
    EMAIL=models.CharField(max_length=250)
    MODULE=models.CharField(max_length=50)
    PIT_SOL_HEADER =models.CharField(max_length=150)
    PIT_SOL_BODY =models.CharField(max_length=500)
    PIT_SOL_IMAGE =models.ImageField(upload_to=upload_imgto, blank=True, null=True)
    PIT_SOL_VIDEO =models.FileField(upload_to=upload_vidto, blank=True, null=True)
    STATUS=models.CharField(max_length=50)
    COMMENTS=models.CharField(max_length=250)
    DESCRIPTION=models.CharField(max_length=250)
    CREATED_USER=models.CharField(max_length=150)
    CREATED_DATE=models.DateField()
    MODIFIED_USER=models.CharField(max_length=150)
    MODIFIED_DATE=models.DateField() 