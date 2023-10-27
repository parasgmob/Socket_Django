from . import views
from django.urls import path


urlpatterns = [
    path('',views.index1,name='index1'),  
]