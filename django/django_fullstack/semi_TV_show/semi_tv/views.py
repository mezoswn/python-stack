from django.shortcuts import render, redirect, HttpResponse
from . models import *
from time import strftime
from django.contrib import messages


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
        title = request.POST['title']
        network = request.POST['network']
        release_date = request.POST['release_date']
        description = request.POST['description']
        
        last = Show.objects.last()
        id = last.id
        time = Show.objects.get(id=id).release_date
        context = {
        "shows": Show.objects.get(id=id),
        "release_date": time.strftime('%Y-%m-%d')
        }
        
        errors = Show.objects.basic_validator(request.POST)

        if len(errors) > 0:
        
            for key, value in errors.items():
                messages.error(request, value)
            
            return redirect('/')
        else:
            # messages.success(request, "Show successfully updated")
            Show.objects.create(title=title,network=network,release_date=release_date,description=description)
        return redirect('showtv/'+str(id))
        
        # if request.method == "POST":
        #     Show.objects.create(title=request.POST["title"], network=request.POST["network"], release_date=request.POST["date"], description=request.POST["desc"] )
        
        # context = {
        # "id" : Show.objects.last(),
        #     }
        # return redirect('/shows/'+str(context['id'].id))

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
        x.release_date = request.POST['release_date']
        x.save()
    return redirect("/shows/"+str(id))

def update(request,id):
    time = Show.objects.get(id=id).release_date
    context = {
        "shows": Show.objects.get(id=id),
        "date": time.strftime('%Y-%m-%d')
    }
    return render(request,'update_page.html',context)

def destroy(request,id):
    Show.objects.get(id=id).delete()
    return redirect('/shows')

