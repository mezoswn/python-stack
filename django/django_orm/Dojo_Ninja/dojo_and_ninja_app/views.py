from dojo_and_ninja_app.models import Dojos, Ninjas
from django.shortcuts import redirect, render

# Create your views here.
def main(request):
    context = {
        "Dojos" : Dojos.objects.all(),
        "Ninjas": Ninjas.objects.all(),
        
    }
    return render(request, 'index.html', context)

def add_dojo(request):
    Dojos.objects.create(name = request.POST['f_name'] , city =request.POST['city'] , state = request.POST['state'])
    return redirect('/')

def add_ninja(request):
    if request.method == "POST":
        Ninjas.objects.create(first_name = request.POST['first_name'] , last_name =request.POST['last_name'] , dojo = Dojos.objects.get(name=request.POST['dojo'])) 
    return redirect('/')

def delete(request):
    if request.method == "POST":
        Dojos.objects.get(name=request.POST['delete']).delete()
    return redirect('/')
    