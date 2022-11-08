import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTING_MODULE', 'orderSystem.setting')

app = Celery('orderSystem')

app.config_from_object('django.conf:setting', namespace='CELERY')

app.autodiscover_tasks()

