from django.shortcuts import render
from time import gmtime, strftime
# Create your views here.

def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p")
    }
    return render(request,'index.html', context)