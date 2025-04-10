# -*- coding: utf-8 -*-
"""gas_utility_project/urls.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14rl4p8_tdbM5_mfF6q9KdZ1bRaTKlj-C
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('accounts.urls')),
    path('service-requests/', include('service_requests.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)