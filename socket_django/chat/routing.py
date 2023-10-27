from django.urls import re_path #advance path mechanism relative path 
from . import consumers
from django.urls import path
from chat.consumers import ChatRoomConsumer,MySyncConsumer

websocket_urlpatterns = [
  path("ws/sc/",MySyncConsumer.as_asgi()),
  re_path(r'ws/chat/(?P<room_name>\w+)/$',ChatRoomConsumer.as_asgi()),
  
] 


# re_path(r'ws/chat/(?P<room_name>\w+)/$',consumers.ChatRoomConsumer),