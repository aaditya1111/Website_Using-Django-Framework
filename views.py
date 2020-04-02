from django.shortcuts import render
from . models import Userinfo
# Create your views here.

def index(request):
    users=Userinfo.objects.all()
    context={'users':users}
    return render(request,'index.html',context)

