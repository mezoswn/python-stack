from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import random
from time import strftime
# Create your views here.
def root(request):
    return render(request,"index.html")

def index(request):
    if 'gold' not in request.session:
        request.session['gold']=0
        request.session['log']=[]
    if request.POST['gold'] == 'farm':
        x=random.randint(10,20)
        request.session['gold']+=x
        log="Earned" + str(x) + "golds from Farm!" + strftime("%Y-%m-%d %H:%M %p")
        request.session['log'].append(log)
    elif request.POST['gold'] == 'cave':
        x=random.randint(5,10)
        request.session['gold']+=x   
        log="Earned" + str(x) + "golds from cave!" + strftime("%Y-%m-%d %H:%M %p")
        request.session['log'].append(log)
    elif request.POST['gold'] == 'house':
        x=random.randint(2,5)
        request.session['gold']+=x
        log="Earned" + str(x) + "golds from house!" + strftime("%Y-%m-%d %H:%M %p")
        request.session['log'].append(log)
    elif request.POST['gold'] == 'casino':
        x=random.randint(-50,50)
        request.session['gold']+=x
        if x>0:
            log="Earned" + str(x) + "golds from casino!" + strftime("%Y-%m-%d %H:%M %p")
            request.session['log'].append(log)
        else:
            log="ouch" + str(x) + "golds from casino has been lost!" + strftime("%Y-%m-%d %H:%M %p")
            request.session['log'].append(log)
    return redirect("/")

def clear(request):
    request.session['gold']=0
    request.session['log']=[]
    return redirect ('/')