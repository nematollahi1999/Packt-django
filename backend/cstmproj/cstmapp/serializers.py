from django.contrib.auth.models import User
from django.db.models import fields
from django.contrib.auth.models import User
from rest_framework import serializers
from cstmapp.models import Plist

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email')

class PlistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plist
        fields = (  'pname',
                    'sellername',
                    'gender',
                    'situation'
        )