# Generated by Django 4.1 on 2022-08-20 08:36

import Campaign_Press.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CampPressModel',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('MTUSER_ID', models.CharField(max_length=250)),
                ('EMAIL', models.CharField(max_length=250)),
                ('MODULE', models.CharField(max_length=50)),
                ('CAMP_PRESS_HEADER', models.CharField(max_length=150)),
                ('CAMP_PRESS_BODY', models.CharField(max_length=500)),
                ('CAMP_PRESS_IMAGE', models.ImageField(blank=True, null=True, upload_to=Campaign_Press.models.upload_imgto)),
                ('CAMP_PRESS_VIDEO', models.FileField(blank=True, null=True, upload_to=Campaign_Press.models.upload_vidto)),
                ('STATUS', models.CharField(max_length=50)),
                ('COMMENTS', models.CharField(max_length=250)),
                ('DESCRIPTION', models.CharField(max_length=250)),
                ('CREATED_USER', models.CharField(max_length=150)),
                ('CREATED_DATE', models.DateField()),
                ('MODIFIED_USER', models.CharField(max_length=150)),
                ('MODIFIED_DATE', models.DateField()),
            ],
        ),
    ]
