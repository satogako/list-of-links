from rest_framework import serializers
from .models import Resource
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)


class ResourceSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    
    class Meta:
        model = Resource
        fields = ('id', 'title', 'author', 'content', 'tags')