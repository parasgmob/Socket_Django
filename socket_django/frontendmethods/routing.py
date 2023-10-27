from . import consumers
from django.urls import path
from frontendmethods.consumers import MySyncConsumer,MyAsyncConsumer

websocket_urlpatterns = [
  path("ws/fsc/",MySyncConsumer.as_asgi()),
  path("ws/fac/",MyAsyncConsumer.as_asgi()),
  
] 