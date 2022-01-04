from django.db import models

# Create your models here.
class Plist(models.Model):
    pname       =models.CharField(max_length=255)
    sellername  =models.CharField(max_length=50)
    gender      =models.CharField(max_length=10)
    situation   =models.CharField(max_length=50)