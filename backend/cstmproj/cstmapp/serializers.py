from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from cstmapp.models import ProductDetails

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email')

class PlistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductDetails
        fields = (  'pname',
                    'sellername',
                    'gender',
                    'situation'
        )
        #managed = False
        #db_table = 'product_details'