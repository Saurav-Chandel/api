from rest_framework import serializers
#from django.shortcuts import Response,HttpResponse

from .models import Hero

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('url','name', 'email')
        #fields='__all__'

    
        


        
        
