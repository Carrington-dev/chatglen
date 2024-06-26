from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/chat-sync/(?P<room_name>\w+)/$", consumers.SyncChatConsumer.as_asgi()),
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.AsyncChatConsumer.as_asgi()),
]