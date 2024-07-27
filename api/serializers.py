from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField
from main.models import PostModel


class PostSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = PostModel
        fields = ['user', 'name', 'body', 'image', 'url']
    
