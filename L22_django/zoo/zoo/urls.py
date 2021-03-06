from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('animals.urls', namespace='animals')),
    path('about/', include('about.urls', namespace='about'))
]
