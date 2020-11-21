from celery import shared_task
import time
from .models import Snake
from django.core.mail import send_mail
import logging
logger = logging.getLogger(__name__)

@shared_task # декоратор shared_task превращает функцию в задачу
def save_snakes():
    time.sleep(2)
    snakes = Snake.objects.all()
    with open('result.txt', 'w', encoding='utf-8') as f:
        for item in snakes:
            f.write(item.name + '\n')

@shared_task
def send_mail_task(subject, text, email):
    # time.sleep(30)
    logger.info(f"Вызван метод send_mail_task с параметрами:{subject}, {text_message}")
    send_mail(subject, text,
              'pikulev.l.v@gmail.com',
              [email],
              fail_silently=False)