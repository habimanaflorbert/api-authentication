from django.db import models

# Create your models here.

class Languages(models.Model):
    name=models.CharField(max_length=255)
    desc=models.TextField()
    doneat=models.TimeField(auto_now=True)

class Climate(models.Model):
    city=models.CharField(max_length=255)
    humid=models.CharField(max_length=255)
    country=models.CharField(max_length=255)
