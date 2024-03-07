from django.shortcuts import render
from rest_framework import generics
from .models import YoutubeVideos, APIKeys
from .serializers import YoutubeVideosSerializer, APIKeySerializer
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination


class YoutubeVideosPagination(PageNumberPagination):
    """
    Pagination class for the YoutubeVideosListView.
    """
    page_size = 10


class YoutubeVideosListView(generics.ListAPIView):
    """
    API view to retrieve a list of YouTube videos.

    Attributes:
        queryset (QuerySet): The set of YoutubeVideos objects to be serialized.
        serializer_class (Serializer): The serializer class for YoutubeVideos.
        pagination_class (Pagination): The pagination class for the view.
        filter_backends (list): The list of filter backends applied to the view.
    """
    queryset = YoutubeVideos.objects.all().order_by('-publish_time')
    serializer_class = YoutubeVideosSerializer
    pagination_class = YoutubeVideosPagination
    filter_backends = [OrderingFilter]


class APIKeyListView(generics.ListCreateAPIView):
    """
    API view to retrieve a list of API keys or create a new API key.

    Attributes:
        queryset (QuerySet): The set of APIKeys objects to be serialized.
        serializer_class (Serializer): The serializer class for APIKeys.
    """
    queryset = APIKeys.objects.all()
    serializer_class = APIKeySerializer
