import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socket_django.settings')

# application = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
import chat.routing
import frontendmethods.routing
import channel_layers.routing
import chat_connect_db.routing
import generic_consumer.routing

application = ProtocolTypeRouter({
    # "http": django_asgi_app,
    'http': get_asgi_application(),
    # Just HTTP for now. (We can add other protocols later.)
    "websocket": AuthMiddlewareStack(
      URLRouter([*chat.routing.websocket_urlpatterns,*frontendmethods.routing.websocket_urlpatterns,
      *channel_layers.routing.websocket_urlpatterns,
      *chat_connect_db.routing.websocket_urlpatterns,
      *generic_consumer.routing.websocket_urlpatterns,]

      )
    ),
})
