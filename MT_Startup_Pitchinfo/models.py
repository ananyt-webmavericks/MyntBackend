from django.db import models
# lets us explicitly set upload path and filename
def upload_to(instance, filename):
    return 'documents/uploadpitch/{filename}'.format(filename=filename)

# Create your models here.
class PitchinfoModel(models.Model):
    ID = models.AutoField(primary_key=True)
    MTUSER_ID = models.CharField(max_length=250)
    EMAIL=models.CharField(max_length=250)
    MODULE=models.CharField(max_length=50)
    PITCH_UPLOAD_DOC=models.FileField(upload_to=upload_to, blank=True, null=True) 
    STATUS=models.CharField(max_length=50)
    COMMENTS=models.CharField(max_length=250)
    DESCRIPTION=models.CharField(max_length=250)
    CREATED_USER=models.CharField(max_length=150)
    CREATED_DATE=models.DateField()
    MODIFIED_USER=models.CharField(max_length=150)
    MODIFIED_DATE=models.DateField()