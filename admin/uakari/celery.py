import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

celery_app = Celery('uakari')
celery_app.config_from_object('settings', namespace='CELERY')
celery_app.autodiscover_tasks()
