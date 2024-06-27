import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
from chatty.routing import websocket_urlpatterns
from channels.layers import get_channel_layer
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatweb.settings')

http_application = get_asgi_application()




application = ProtocolTypeRouter({
    "http": http_application,
    # Just HTTP for now. (We can add other protocols later.)
    "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        ),
})

channel_layer = get_channel_layer()