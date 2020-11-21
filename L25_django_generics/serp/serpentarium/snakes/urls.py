from django.urls import path
from .views import status_view # index_view
from .views import SnakesListView, ContactFormView

app_name = 'snakes'

urlpatterns = [
    # path('', index_view, name='index'),
    path('', SnakesListView.as_view(), name='index'),
    path('status/', status_view, name='status'),
    path('contact/', ContactFormView.as_view(), name='contact'),
]
