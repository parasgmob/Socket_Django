from django.shortcuts import render

# Create your views here.


def index(request):
  return render(request,'index2.html',{})


#creating dynamic group name
def group_index(request,group_name):
  print("Group Name...",group_name)
  return render(request,'index2.html',{'groupname':group_name})  #is view se index file me jayega group_name aur ws request me bhejenge group name ws url se group name leke consumer tak aur fir consumer me group_name se group bna lenge  