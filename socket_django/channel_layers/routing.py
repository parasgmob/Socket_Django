from . import consumers
from django.urls import path
from channel_layers.consumers import *

websocket_urlpatterns = [
  path('ws/chl/sc/<str:groupkaname>/',MyChannelsSyncConsumer.as_asgi()),
  path('ws/chl/ac/',MyChannelsAsyncConsumer.as_asgi()),
]

# MyChannelsAsyncConsumer