from django.core.mail import send_mail
from django.shortcuts import render
from .models import Snake
import time
from .tasks import save_snakes, send_mail_task
from celery import current_app




# Create your views here.
def index_view(request):
    # snakes = Snake.objects.all()
    snakes = Snake.objects.select_related('specia__family').all()
    # snakes = Snake.objects.prefetch_related('specia__family').all()
    context = {"snakes": snakes}
    if request.method == 'POST':
        # print(time.time())
        # save_snakes.delay()
        # print(time.time())
        result = send_mail_task.delay('celery_topic', 'celery_text')
        context['task_id'] = result.id

    return render(request, 'snakes/index.html', context)

def status_view(request):
    task_id = request.GET['task_id']
    # status = 'done'
    task = current_app.AsyncResult(task_id)
    status = task.status
    # status = None
    
    context = {"status": status, "task_id": task_id}
    return render(request, "snakes/status.html", context)
