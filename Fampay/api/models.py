from django.db import models

class YoutubeVideos(models.Model):
    """
    Model to store information about YouTube videos.
    """
    video_id = models.CharField(max_length=50, unique=True)
    title = models.TextField(max_length=255)
    description = models.TextField()
    publish_time = models.DateTimeField()
    thumbnail_url = models.URLField()

    def __str__(self):
        """
        String representation of the YoutubeVideos instance.
        """
        return self.title


class APIKeys(models.Model):
    """
    Model to store API keys and their quota limit status.
    """
    key = models.CharField(max_length=50)
    quota_limit_reached = models.BooleanField(default=False)

    def __str__(self):
        """
        String representation of the APIKeys instance.
        """
        return self.key
