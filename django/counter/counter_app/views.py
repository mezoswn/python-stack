from django.shortcuts import redirect, render

count3=0


def index(request):
    request.session['counter']=0
    # print('hello')
    return redirect('/to')

def real(request):
    request.session['counter2']=0
    return redirect['/to']


def some_function(request):
    # print("hi there")
    count = request.session['counter'] 
    count = count + 1
    request.session['counter']=count
    request.session['counter2'] += 1

    #count2 = request.session['counter2'] 
    #
    # request.session['counter2']=count2

    context={'counter':request.session['counter'],
            #'counter2':count3

    }
    return render(request,"show.html",context)

def destroy(request):
    return redirect('/')

def plustwo(request):
    # print("hi there")
    request.session['counter']+=1
    context={'counter':request.session['counter']

    }
    return redirect('/to')