from . import consumers
from django.urls import path
from generic_consumer.consumers import *

websocket_urlpatterns = [
  path('ws/wsc/<str:groupkaname>/',MyWebsocketConsumer.as_asgi()),
  path('ws/wac/<str:groupkaname>/',MyAsyncWebsocketConsumer.as_asgi()),
]
