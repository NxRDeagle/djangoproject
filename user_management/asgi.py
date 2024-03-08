import os
from django.core.asgi import get_asgi_application
# ASGI - (Asynchronous Server Gateway Interface) позволяют Django использовать асинхронный режим 
# для улучшения обработки запросов и выполнения задач, требующих больше времени

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_management.settings')

application = get_asgi_application()
