from django.db import models
 
# lets us explicitly set upload path and filename
def upload_to(instance, filename):
    return 'images/caminvestor/{filename}'.format(filename=filename)

# Create your models here.
class CamInvestorModel(models.Model):
    ID = models.AutoField(primary_key=True)
    MTUSER_ID = models.CharField(max_length=250)
    EMAIL=models.CharField(max_length=250)
    MODULE=models.CharField(max_length=50)
    CINV_SNO=models.CharField(max_length=50)
    CINV_MEMBER_NAME=models.CharField(max_length=150)
    CINV_MEMBER_POSITION=models.CharField(max_length=150)
    CINV_FB_LINK=models.CharField(max_length=150)
    CINV_INSTA_LINK=models.CharField(max_length=150)
    CINV_LINKEDIN_LINK=models.CharField(max_length=150)
    CINV_BIO=models.CharField(max_length=500)
    CINV_PROFILE_PIC=models.ImageField(upload_to=upload_to, blank=True, null=True)
    STATUS=models.CharField(max_length=50)
    COMMENTS=models.CharField(max_length=250)
    DESCRIPTION=models.CharField(max_length=250)
    CREATED_USER=models.CharField(max_length=150)
    CREATED_DATE=models.DateField()
    MODIFIED_USER=models.CharField(max_length=150)
    MODIFIED_DATE=models.DateField()