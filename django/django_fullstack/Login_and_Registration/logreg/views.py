from django.shortcuts import redirect, render
from .models import*
from django.contrib import messages
from datetime import date, datetime, timedelta
from django.utils import timezone

def home(request):
    request.session['user'] = ""
    return render(request,"index.html")

def create(request):
    errors = Users.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect("/")
    else:
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['passwd']
        confpw = request.POST['confirmpwd']
        birthDate = request.POST['birth_date']
        try:
            if Users.objects.get(email=email):
                errors['retitle'] = "oops! This email is already exist"
        except:
            pass

        if password == confpw :
            Users.objects.create(first_name=firstname,last_name=lastname,email=email,password=password)
            data={
            "fname":firstname,
            "lastname":lastname,
            "email":email,
            "password":password,
            "birth_date":birthDate            
            }
            request.session['user'] = data
            return redirect ("/success")
        return redirect("/")

def login(request):
    email = request.POST['loginemail']
    passwd = request.POST['loginpass']
    user = Users.objects.filter(email=email)
    if len(user) == 0:
        return redirect("/")
    user = user.first()
    if user.password != passwd:
        return redirect("/")
    data = {
        'fname' : user.first_name,
        'password' : user.password,
        'email' : user.email,
        'lastname' : user.last_name,
    }
    request.session['user'] = data
    return redirect("/success")

def welcome(request):
    if request.session['user']:
        user = request.session['user']
        return render(request,"success.html",user)
    return redirect("/")

def logout(request):
    if request.session['user']:
        request.session.clear()
        return redirect("/")