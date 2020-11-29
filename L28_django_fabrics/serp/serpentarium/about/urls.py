from django.urls import path
from .views import AboutTemplateView #,about_view

app_name = 'about'

urlpatterns = [
    # path('', about_view, name='about'),
    path('', AboutTemplateView.as_view(), name='about'),
]
