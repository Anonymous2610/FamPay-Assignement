from celery import shared_task
from .services import get_latest_videos

@shared_task(bind=True)
def fetch_latest_videos(self):
    """
    Celery task to fetch and process the latest videos based on the provided query.
    
    Args:
        self: Instance of the Celery task.
        
    Returns:
        str: A string indicating the completion status ('Done').
    """
    get_latest_videos()
    return "Done"
