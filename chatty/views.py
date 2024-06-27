# chat/views.py
from django.shortcuts import render

from django.http import JsonResponse
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from chatty.consumers import SyncChatConsumer

def index(request):
    return render(request, "chatty/index.html")


def room(request, room_name):
    print(room_name)
    return render(request, "chatty/room.html", {"room_name": room_name})


@api_view(["POST", "GET"])
def send_message(request, room_name):
    if request.method == "POST":
        # print(request.data)
        # data = request.POST.get('data')
        data = request.data["message"]
        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(
            f"chat_{room_name}",
            {
                "type": "send_message",
                "message": data,
            }
        )
        # SyncChatConsumer().chat_message(request.data)
        return Response({'status': 'Data sent to WebSocket', "message": data})
    return Response({'status': "Nothing sent to this endpoint"})
