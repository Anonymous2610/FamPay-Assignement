from django.db import models

# Create your models here.

class YoutubeVideos(models.Model):
    video_id = models.CharField(max_length=50, unique=True)
    title = models.TextField(max_length=255)
    description = models.TextField()
    publish_time = models.DateTimeField()
    thumbnail_url = models.URLField()

    def __str__(self):
        return self.title

class APIKeys(models.Model):
    key = models.CharField(max_length=50)
    quota_limit_reached = models.BooleanField(default=False)

    def __str__(self):
        return self.key