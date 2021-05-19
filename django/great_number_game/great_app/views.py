from django.shortcuts import redirect, render, HttpResponse

# Create your views here.

import random
c= random.randint(1, 100)

def init(request):
    request.session['counter']=0
    return redirect('')
    
def theprime(request):
    print(c)
    return render(request,"prime.html")



# def con(request):
#     return redirect('post/index')

def index(request):
    
    
    x=int(request.POST['number'])
    print(c)
    context={'numberr':x
            
                

    }
    if x>c:

        return render(request,"high.html")
    elif (x<c):
        return render(request,"low.html")
    elif (x==c):
        return render(request,"equal.html",context)
