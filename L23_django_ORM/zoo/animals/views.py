from django.shortcuts import render
from .models import Animal
#
#
def index_view(request):
    animals = Animal.objects.select_related('kind', 'kind__family').all()
    # animals = Animal.objects.prefetch_related('foods').all()
    return render(request, 'animals/index.html', {'animals': animals})
