"""
serpentarium URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

import debug_toolbar
from django.conf import settings

# from django.conf.urls.static import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from .settings import MEDIA_URL, MEDIA_ROOT


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('snakes.urls', namespace='snakes')),
    path('about/', include('about.urls', namespace='about')),
    path('__debug__/', include(debug_toolbar.urls)),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += staticfiles_urlpatterns()
