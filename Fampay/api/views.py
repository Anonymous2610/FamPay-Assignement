from django.shortcuts import render
from rest_framework import generics
from .models import YoutubeVideos, APIKeys
from .serializers import YoutubeVideosSerializer, APIKeySerializer
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination


class YoutubeVideosPagination(PageNumberPagination):
    page_size = 10

class YoutubeVideosListView(generics.ListAPIView):
    queryset = YoutubeVideos.objects.all().order_by('-publish_time')
    serializer_class = YoutubeVideosSerializer
    pagination_class = YoutubeVideosPagination
    filter_backends = [OrderingFilter]


class APIKeyListView(generics.ListCreateAPIView):
    queryset = APIKeys.objects.all()
    serializer_class = APIKeySerializer