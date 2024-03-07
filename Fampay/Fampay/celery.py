from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fampay.settings')

# Create a Celery instance and configure it using the settings from Django.
app = Celery('Fampay')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Define periodic tasks (Celery Beat schedule).
app.conf.beat_schedule = {
    'run_every_10_seconds': {
        'task': 'api.tasks.fetch_latest_videos',  # Task to be executed
        'schedule': 10.0,  # Every 10 seconds
    },
}

# Automatically discover tasks in all installed apps.
app.autodiscover_tasks()

# Celery debug task for testing.
@app.task(bind=True)
def debug_task(self):
    """
    Celery task for debugging purposes.

    Args:
        self: Instance of the Celery task.

    Returns:
        None
    """
    print(f'Request: {self.request!r}')
