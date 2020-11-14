import time

from django.core.mail import send_mail
from django.shortcuts import render
from .models import Animal
from .tasks import save_animal, send_mail_task
import time
from celery import current_app


def index_view(request):
    context = {}
    animals = Animal.objects.select_related('kind', 'kind__family').all()
    context['animals'] = animals
    if request.method == 'POST':
        # print(time.time())
        # save_animal.delay()
        # print(time.time())
        result = send_mail_task.delay('scelery', 'stext')
        context['task_id'] = result.id
        # print(result.status)

    # animals = Animal.objects.prefetch_related('foods').all()

    return render(request, 'animals/index.html', context)


def status_view(request):
    task_id = request.GET['task_id']
    # По id получить задачу
    task = current_app.AsyncResult(task_id)
    status = task.status
    return render(request, 'animals/status.html', {'status': status, 'task_id': task.id})

