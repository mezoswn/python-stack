from django.shortcuts import redirect, render
from .models import*
from django.contrib import messages
from datetime import date, datetime, timedelta
from django.utils import timezone
def home(request):
    request.session['user'] = ""
    request.session['mymessages'] = ""
    return render(request,"home.html")
def createuser(request):
    errors = User.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        passwd = request.POST['passwd']
        confpw = request.POST['confirmpw']
        birthDate = request.POST['birth_date']
        try:
            if User.objects.get(email=email):
                errors["retitle"] = "this email is already exist"
        except:
            pass
        if passwd == confpw :
            User.objects.create(first_name=firstname,last_name=lastname,email=email,passwod=passwd)
            data ={
                "fname":firstname,
                "lastname":lastname,
                "email": email,
                "pass":passwd,
                "birth_date": birthDate
            }
            request.session['user'] = data
            return redirect('/welcome')
        return redirect("/")
def login(request):
    errors = User.objects.login_Validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        email = request.POST['loginemail']
        passwd = request.POST['loginpass']
        users = User.objects.filter(email=email)
        
        if len(users) == 0:
            return redirect("/")
        user = users.first()
        if user.passwod != passwd:
            return redirect("/")
        data ={
            'fname' : user.first_name,
            'password':user.passwod,
            'email' : user.email,
            'lastname' : user.last_name,
            'userid':user.id
        }
        request.session['user']= data
        return redirect("/welcome")

def welc(request):
    all_messages = Messages.objects.all()
    #all_comment = Comments.objects.all()
    if request.session['user'] :
        user = request.session['user']
        data={
        'my_massege':all_messages,
        'user':user,
        #'comments':all_comment
        }
        
        return render(request,"welcome.html",data)
    return redirect('/')
def logout(request):
    if request.session['user']:
        request.session.clear()
        return redirect('/')
def creatmessage(request):
    users = User.objects.filter(first_name = request.session['user']['fname'])
    user = users[0]
    message =request.POST['messagearea']
    if len(message) != 0:
        Messages.objects.create(message =  message, user = user )
        #all_messages = Messages.objects.all()
        data = {
            "mymessag" : message,
            
        }
        request.session['mymessages'] = data
        return redirect('/welcome')
def delete_message(request,id):
    users = User.objects.filter(first_name = request.session['user']['fname'])
    user = users[0]
    message_for_delete = Messages.objects.filter(id=id , user = user  )
    message_for_delete.delete()
    return redirect('/welcome')

def showComment(request,id):
    all_messages = Messages.objects.filter(id=id)
    all_messages.first()
    users = request.session['user']
    myCommints = Comments.objects.filter(message = all_messages[0] )
    if request.session['user']:
        user = request.session['user']
        data={
        'my_commints':myCommints,
        'user':user,
        'my_massege': all_messages
        }
    return render(request,'profile.html',data)
def createComment(request,id):
    comment = request.POST['mycomment']
    users = User.objects.filter(first_name = request.session['user']['fname'])
    user = users[0]
    messages = Messages.objects.filter(id = id)
    message = messages.first()
    Comments.objects.create(comment = comment ,user = user , message = message )
    return redirect('/welcome')
def deletcomment(request,id):
    users = User.objects.filter(first_name = request.session['user']['fname'])
    user = users[0]
    Commentfordelet = Comments.objects.filter(id=id , user = user) 
    Commentfordelet.delete()
    return redirect('/welcome')

