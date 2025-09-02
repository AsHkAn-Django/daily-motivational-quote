import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quote_collection.settings')
app = Celery('quote_collection')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.beat_scheduler = 'django_celery_beat.schedulers:DatabaseScheduler'    # new
app.conf.timezone = 'UTC'    # new
app.autodiscover_tasks()