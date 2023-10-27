from . import consumers
from django.urls import path
from chat_connect_db.consumers import *

websocket_urlpatterns = [
  path('ws/db/sc/<str:groupkaname>/',MyDbSyncConsumer.as_asgi()),
  path('ws/db/ac/<str:groupkaname>/',MyChannelsAsyncConsumer.as_asgi()),
]
