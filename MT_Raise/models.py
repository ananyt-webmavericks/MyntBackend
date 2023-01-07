from django.db import models
 
# lets us explicitly set upload path and filename
def upload_to(instance, filename):
    return 'documents/raisedocs/{filename}'.format(filename=filename)

# Create your models here.
class RaiseModel(models.Model):
      ID = models.AutoField(primary_key=True)
      MTUSER_ID = models.CharField(max_length=250)
      EMAIL=models.CharField(max_length=250)
      MODULE=models.CharField(max_length=50)
      RAISE_NAME=models.CharField(max_length=150)
      RAISE_EMAIL=models.CharField(max_length=150)
      RAISE_FOUNDER_URL1=models.CharField(max_length=250)
      RAISE_FOUNDER_URL2=models.CharField(max_length=250, blank=True, null=True)
      RAISE_COMPANY_NAME=models.CharField(max_length=250)
      RAISE_COM_LINKPAGE=models.CharField(max_length=250)
      RAISE_WEBSITE=models.CharField(max_length=250)
      RAISE_FUNDRAISING=models.CharField(max_length=500)
      RAISE_PROD_DESC=models.CharField(max_length=500)
      RAISE_TRACTION=models.CharField(max_length=500)
      RAISE_REVENUE=models.CharField(max_length=500)
      RAISE_TEAM=models.CharField(max_length=500)
      RAISE_COMROUND=models.CharField(max_length=500)
      RAISE_MTRIGHTS=models.CharField(max_length=500)
      RAISE_EXIST_COM=models.CharField(max_length=500)
      RAISE_PRIVATEROUND=models.CharField(max_length=50)
      RAISE_UPLOAD_DOC=models.FileField(upload_to=upload_to, blank=True, null=True)
      STATUS=models.CharField(max_length=50)
      COMMENTS=models.CharField(max_length=250)
      DESCRIPTION=models.CharField(max_length=250)
      CREATED_USER=models.CharField(max_length=150)
      CREATED_DATE=models.DateField()
      MODIFIED_USER=models.CharField(max_length=150)
      MODIFIED_DATE=models.DateField()