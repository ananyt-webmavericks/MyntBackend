# Generated by Django 4.1 on 2022-08-10 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MT_Startup_Banner_Dets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannermodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
