from django.urls import path
from .views import index_view, status_view

app_name = 'animals'

urlpatterns = [
    path('', index_view, name='index'),
    path('status/', status_view, name='status'),
]
