from django.shortcuts import render, redirect
from . models import *

# Create your views here.
def shows(request):
    context = {
        "shows" : Show.objects.all(),
    }
    return render(request,'index.html',context)

def index(request):
    return redirect('/shows')

def create(request):
    return render(request,'create_page.html')

def add(request):
        if request.method == "POST":
            Show.objects.create(title=request.POST["title"], network=request.POST["network"], release_date=request.POST["date"], description=request.POST["desc"] )
        
        context = {
        "id" : Show.objects.last(),
            }
        return redirect('/shows/'+str(context['id'].id))

def read(request,id):
    context = {
        "shows" : Show.objects.get(id=id),
    }
    return render(request,'read_page.html',context)

def edit(request,id):
    x= Show.objects.get(id=id)
    if request.method == "POST":
        x.title = request.POST['title']
        x.network = request.POST['network']
        x.description = request.POST['desc']
        x.date = request.POST['release_date']
        x.save()
    return redirect("/shows/"+str(id))

def update(request,id):
    context = {
        "shows": Show.objects.get(id=id),
    }
    return render(request,'update_page.html',context)

def destroy(request,id):
    Show.objects.get(id=id).delete()
    return redirect('/shows')

