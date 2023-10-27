"""socket_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include


# schema_view = get_schema_view(
#     openapi.Info(
#         #  add your swagger doc title
#         title="Solidity Finance",
#         #  version of the swagger doc
#         default_version='v1',
#         # first line that appears on the top of the doc
#         description="APIs for Solidity Finance",
#     ),
#     generator_class=BothHttpAndHttpsSchemaGenerator,
#     public=True,
# )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/',include('chat.urls')),
    path('fr/',include('frontendmethods.urls')),
    path('ch/',include('channel_layers.urls')),
    path('connectdb/',include('chat_connect_db.urls')),
    path('gen/',include('generic_consumer.urls')),
]
