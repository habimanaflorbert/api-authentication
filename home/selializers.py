from home.models import Languages
from django.contrib.auth import models
from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from .models import *

class UserSeliarizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=['url','username','email','is_active']
    
class LangSeliarizer(serializers.ModelSerializer):
    class Meta:
        model=Languages
        fields=('__all__')
        
class ClimatSeliarizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Climate
        fields=['url','city','humid','country']