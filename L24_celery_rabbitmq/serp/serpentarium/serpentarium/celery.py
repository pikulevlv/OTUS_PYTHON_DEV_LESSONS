import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'serpentarium.settings')
celery_app = Celery('serpentarium_c')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks() # сама найдет отложенные задачи