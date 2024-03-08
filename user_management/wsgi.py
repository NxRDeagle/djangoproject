import os
from django.core.wsgi import get_wsgi_application
# WSGI-сервера - (Web Server Gateway Interface) чтобы обрабатывать множество запросов одновременно

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_management.settings')

application = get_wsgi_application()
