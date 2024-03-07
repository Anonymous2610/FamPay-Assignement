from rest_framework import serializers
from .models import YoutubeVideos, APIKeys

class YoutubeVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeVideos
        fields = '__all__'

class APIKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = APIKeys
        fields = '__all__'