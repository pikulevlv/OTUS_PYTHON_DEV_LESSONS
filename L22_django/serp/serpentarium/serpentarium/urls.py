"""
serpentarium URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('snakes.urls', namespace='snakes')),
    path('about/', include('about.urls', namespace='about')),
]
