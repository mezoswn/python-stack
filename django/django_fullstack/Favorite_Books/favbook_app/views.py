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
            'userid':user.id,
            
        }
        request.session['user'] = data
        return redirect('/welcome')

def welc(request):
    books = Book.objects.all()
    if request.session['user'] :
        user = request.session['user']
        data={
        'user':user,
        'books':books,
        
        }
        return render(request,"welcome.html",data)
    return redirect('/')
def logout(request):
    if request.session['user']:
        request.session.clear()
        return redirect('/')
def addBook(request , id):
    title = request.POST['titletext']
    users = User.objects.filter(id= id)
    user = users.first()
    desc = request.POST['desc']
    book = Book.objects.create(title = title , uploaded_by = user , desc = desc)
    context= {
        "Booktitle" :book.title,
        "Booktitle" :book.uploaded_by.first_name +" "+ book.uploaded_by.last_name,
        'bookids':book.id,
        'desc' : desc
        }
    return render(request,'favorite.html',context)
def deleteBook(request,id):
    books = Book.objects.filter(id=id)
    book_todelete = books.first()
    book_todelete.delete()
    return redirect('/welcome')
def showFave(request,id):
    user = request.session['user']
    book = Book.objects.get(id=id)
    bookid = book.id
    booktitle = book.title
    bookuploadedby = book.uploaded_by
    usersLiked = book.users_who_like.all()
    desc = book.desc
    context = {
        'Booktitle' : booktitle,
        'BookAuthor': bookuploadedby,
        'userswholike':usersLiked,
        'bookid':bookid,
        'desc':desc,
        'user':user,
        'uploaded_by': Book.objects.first().uploaded_by
    }
    return render(request,'favorite.html',context)
def addFavarit(request,id):
    users = request.session['user']
    user = User.objects.get(id = users['userid'])
    books = Book.objects.filter(id=id)
    book = books.first().id
    user.liked_books.add(book)
    return redirect('/welcome')
def updatedes(request,id):
    desc= request.POST['updatetext']
    Book.objects.update(id=id , desc = desc)
    return redirect('/showbook/'+str(id))
def deletedes(request):
    request.session['description'] = ""
    return redirect('/showbook')
def unfavarit(request,id):
    users = request.session['user']
    user = User.objects.get(id = users['userid'])
    books = Book.objects.filter(id=id)
    book = books.first().id
    user.liked_books.remove(book)
    return redirect('/welcome')


