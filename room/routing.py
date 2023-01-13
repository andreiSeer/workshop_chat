
from . import consumers

from django.urls import path

websocket_urlpatterns = [
    path('ws/<str:room_name>/',consumers.ChatConsumer.as_asgi()),
    path('ws/listen-room-update/<str:room_name>/',consumers.RoomConsumer.as_asgi()),
]