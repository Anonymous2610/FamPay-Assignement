from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fampay.settings')

app = Celery('Fampay')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.beat_schedule = {
    'run_every_10_seconds': {
        'task': 'api.tasks.fetch_latest_videos',
         'schedule': 10.0,  # Every 10 seconds
    },
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
