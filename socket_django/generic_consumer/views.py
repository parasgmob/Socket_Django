from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request,group_name):
  return render(request,'index4.html',{'groupname':group_name})
