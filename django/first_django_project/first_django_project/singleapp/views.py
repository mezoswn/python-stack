from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

# Create your views here.
def root(request):
    return redirect("/blogs")

def index(request):
    string = "placeholder to later display a list of all blogs"
    return HttpResponse(string)

def new(request):
    string = "placeholder to display a new form to create a new blog"
    return HttpResponse(string)

def create(request):
    return redirect('/')

def show(request, number):
    number = str(number)
    string = "placeholder to display blog number: " + number
    return HttpResponse(string)

def edit(request, number):
    number = str(number)
    string = "placeholder to edit blog " + number
    return HttpResponse(string)

def destroy(request, number):
    return redirect("/blogs")

def json(request):
    return JsonResponse({
        "title" : "Django",
        "content": "a framework"
    })