from django.shortcuts import render
from .models import Group,ChatModel

# Create your views here.
def index1(request,group_name):
  print(group_name)
  group = Group.objects.filter(name = group_name).first()
  chats=[]
  if group:
    chats= ChatModel.objects.filter(group=group)
  else:
    group = Group(name = group_name)
    group.save()
  return render(request,'index3.html',{'groupname':group_name,'chats':chats})