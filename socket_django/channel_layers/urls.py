from . import views
from django.urls import path


urlpatterns = [
    path('',views.index,name='index'),
    path('gr/<str:group_name>/',views.group_index,name='group_index'),#creating dynamic path for dynamic group name
]