import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatweb.settings')

http_application = get_asgi_application()




application = ProtocolTypeRouter({
    "http": http_application,
    # Just HTTP for now. (We can add other protocols later.)
})