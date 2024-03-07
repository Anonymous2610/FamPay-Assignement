from celery import shared_task
from .services import get_latest_videos


@shared_task(bind = True)
def fetch_latest_videos(self):  # Default query
    """Fetches and processes latest videos based on the provided query."""
    get_latest_videos()
    # for i in range(10):
    #     print(i)
    return "Done"


