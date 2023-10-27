from django.contrib import admin
from .models import ChatModel,Group

# Register your models here.

class ShowChat(admin.ModelAdmin):
  list_display = ('id','content','cratetime','group')

@admin.register(Group)
class ShowGroup(admin.ModelAdmin):
  list_display = ['id','name']

admin.site.register(ChatModel,ShowChat)
