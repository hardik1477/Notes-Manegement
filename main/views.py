from django.http import HttpResponse
from django.shortcuts import render
from .models import files
import sqlite3


def home(request):
    return render(request,'homepage.html')

def right(request ,fullname , mail):
    return render(request , 'mainhome.html' ,{'files' : files.objects.all() , 'fullname' : fullname , 'mail' : mail})
# Create your views here.

def note(request):
    return render(request , 'notes.html' , {'id' : int(request.GET["id"]) , 'y' : files.objects.all() , 'fullname' : request.GET["fullname"] })

def save(request):  
    for i in files.objects.all() :
        if i.id == int(request.GET["id"]) :
            i.txt = request.GET["text"]
            i.name = request.GET["name"]
            i.save()
            return render(request , 'mainhome.html' , {'files' : files.objects.all() , 'fullname' : request.GET["fullname"] , 'mail' : i.email})
    return HttpResponse("hello")

def delete (request):
    for i in files.objects.all():
        if i.id == int(request.GET["id"]):
            x = i.email
            i.delete()
            return render(request , 'mainhome.html' , {'files' : files.objects.all() , 'fullname' : request.GET["fullname"] , 'mail' : i.email , 'id' : int(request.GET["id"])})
    
def create1(request):
    return render (request , 'new.html' ,{'txt' : "" , 'count' : 0 , 'files' : files.objects.all() , 'fullname' : request.GET["fullname"] ,'mail' : request.GET['mail']})


def savenew(request):
    if(request.GET["filename"] == ""):
        return render(request , 'new.html' , {'txt' : request.GET["text"] , 'count' : 1 , 'mail' : request.GET["mail"], 'filename' : ""})

    for i in files.objects.all():
        if i.email == request.GET["mail"] and i.name == request.GET["filename"]:
             return render(request , 'new.html' , {'txt' : request.GET["text"] , 'count' : 2 , 'mail' : request.GET["mail"], 'filename' : request.GET["filename"]})
    x = files()
    x.email = request.GET["mail"]
    x.name = request.GET["filename"]
    x.txt =  request.GET["text"]
    x.fileinput = "x"
    x.save()
    return render(request , 'mainhome.html' , {'files' : files.objects.all() , 'fullname' : request.GET["fullname"] , 'mail' : x.email})
