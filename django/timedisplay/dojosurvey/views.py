from django.http import request
from django.shortcuts import render, HttpResponse

def index(request):
    return render(request,"dojohtml.html")

def thepoint(request):
    context={
    'name':request.POST['name'],
    'location':request.POST['location'],
    'comment':request.POST['comment'],
    'lang':request.POST['lang'],
    }
    return render(request,"show.html",context)