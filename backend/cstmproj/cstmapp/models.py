from django.db import models

# Create your models here.
#class Plist(models.Model):
    #pname       =models.CharField(max_length=255)
    #sellername  =models.CharField(max_length=50)
    #gender      =models.CharField(max_length=10)
    #situation   =models.CharField(max_length=50)

class ProductDetails(models.Model):
    pname = models.CharField(max_length=255)
    sellername = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    situation = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'product_details'

    
#class ProductDetails(models.Model):
    #pname = models.CharField(max_length=255, blank=True, null=True)
    #sellername = models.CharField(max_length=50, blank=True, null=True)
    #gender = models.CharField(max_length=10, blank=True, null=True)
    #situation = models.CharField(max_length=50, blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'product_details'