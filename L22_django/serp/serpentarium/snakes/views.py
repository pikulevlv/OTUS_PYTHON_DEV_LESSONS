from django.shortcuts import render
from .models import Snake

# Create your views here.
def index_view(request):
    snakes = Snake.objects.all()
    context = {"snakes":snakes}
    return render(request, 'snakes/index.html', context)