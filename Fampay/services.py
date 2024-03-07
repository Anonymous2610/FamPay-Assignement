# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from datetime import datetime, timedelta
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fampay.settings')
django.setup()
def get_last_published_time():
    from api.models import APIKeys, YoutubeVideos
    latest_video = YoutubeVideos.objects.order_by('-publish_time').first()
    # Calculate 'publishedAfter' parameter
    if latest_video:
        published_after = latest_video.publish_time
    else:
        # If no videos are stored, fetch videos from the last 24 hours
        published_after = datetime.utcnow() - timedelta(days=1)

    # Format 'publishedAfter' as required by the YouTube API
    published_after_str = published_after.isoformat() + 'Z'
    return published_after_str


def save_youtube_video(data):
    from api.models import APIKeys, YoutubeVideos
    video_id = data['id']['videoId']
    title = data['snippet']['title']
    description = data['snippet']['description']
    publish_time = datetime.strptime(data['snippet']['publishedAt'], "%Y-%m-%dT%H:%M:%SZ")
    thumbnail_url = data['snippet']['thumbnails']['default']['url']

    # Create or update the instance
    video, created = YoutubeVideos.objects.update_or_create(
        video_id=video_id,
        defaults={
            'title': title,
            'description': description,
            'publish_time': publish_time,
            'thumbnail_url': thumbnail_url,
        }
    )

    return video, created

def main(query,max_results=10):
    from api.models import APIKeys, YoutubeVideos
    API_KEY = APIKeys.objects.filter(quota_limit_reached=False).first()
    if API_KEY == None:
        print("All API keys are exhausted. Add new API keys")
        #NOTIFY USER LOGIC TO BE ADDED e.g, Email the user to add API keys
        return 
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                                developerKey=API_KEY)

    time = get_last_published_time()
    request = youtube.search().list(
        q=query,
        part="snippet",
        order="date",
        publishedAfter= time,
        maxResults=max_results,
        type="video"
    )
    try:
        response = request.execute()
            # Retrieve the timestamp of the latest stored video
        for item in response.get('items', []):
            video, created = save_youtube_video(item)
            if created:
                print(f"New video saved: {video}")
            else:
                print(f"Video already exists: {video}")
        return
    except HttpError as e:
        error_code = e.resp.status
        error_content = e.content.decode("utf-8")
        print(f"HTTP error {error_code}: {error_content}")
        return


if __name__ == "__main__":
    query = "cricket"
    main(query)