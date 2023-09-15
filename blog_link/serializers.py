from rest_framework import serializers
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)
from .models import Resource



class ResourceSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    author = serializers.SerializerMethodField()
    
    
    class Meta:
        model = Resource
        fields = ('id', 'title', 'url', 'author', 'content', 'updated_on', 'site_screenshot', 'admirers', 'tags')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['content'] = instance.content.replace('<p>', '').replace('<br>', '').replace('</p>', '')
        return representation

    def get_author(self, obj):
        return obj.author.username