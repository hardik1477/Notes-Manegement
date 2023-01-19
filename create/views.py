from urllib import request
from django.shortcuts import render
from .models import users , forgot
from main.views import right
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.


def login(request):
    return render(request , 'loginpage.html')


def logged(request):
    x = users.objects.all()
    for i in x:
        if i.email == request.POST["email"] and check_password( request.POST["password"],i.password ) : 
            return right(request ,i.name + "  " +i.surname,i.email)
    return render(request , 'loginpage.html' ,{'x' : 1}) 


def signup(request):
    return render(request , 'form.html' ,{'password':"", 'uname' : ""  , 'usurname' : "" , 'uemail' :"" , 'ubfname' :"" , 'x' : 0})


def forgotn(request , dict = {'x' : 0 , 'y' : forgot.objects.all()}):
    return render(request ,'forgot.html' , dict)

class recovery :
    def __init__(self) -> None:
        self.m = ""

    def forgotpassword(self , request):
        x = forgot.objects.all()
        for i in x:
            if i.email == request.POST["email"] and i.friend_name == request.POST["bestfriend_name"]:
                self.m = i.email
                return render(request ,'newpassword.html')
        return forgotn(request , {'x' : 1 , 'y' : x})

    def recoveryover(self, request):
        if request.POST["password"] != request.POST["confirmpass"] :
            return render(request , 'newpassword.html')
        for i in users.objects.all() :
            if i.email == self.m :
                i.password = make_password(request.POST["password"])
                fullname = i.name + "  " +i.surname
                i.save()
                break
        return right(request ,fullname , self.m)

def register(request):
    if request.POST["password"] != request.POST["confirmpass"] :
        dict =  {
            'uname' :request.POST["name"] ,
            'usurname' : request.POST["surname"] ,
            'uemail': request.POST["email"],
            'ubfname'  : request.POST["best_friendname"],
            'x' : 0}
        return render(request , 'form.html',dict)
    for i in users.objects.all():
        if i.email == request.POST["email"]:
            dict =  {
            'uname' :request.POST["name"] ,
            'usurname' : request.POST["surname"] ,
            'uemail': request.POST["email"],
            'ubfname'  : request.POST["best_friendname"],
            'x' : 1}
            return render(request , 'form.html' , dict)
    h = forgot()
    h.email = request.POST["email"]
    h.friend_name = request.POST["best_friendname"]
    h.save()
    h = users()
    h.email = request.POST["email"]
    h.name = request.POST["name"]
    h.surname = request.POST["surname"]
    x = make_password( request.POST["password"])
    h.password = x
    h.save()
    return right(request ,h.name +"  " + h.surname , h.email)