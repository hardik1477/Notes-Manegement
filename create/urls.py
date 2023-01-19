from django.contrib import admin
from django.urls import path , include
from . import views
from .views import recovery

x = recovery()
urlpatterns = [
    path('login',views.login),
    path('loggedhome' , views.logged),
    path('signup',views.signup),
    path('forgot',views.forgotn),
    path('forgotpassword', x.forgotpassword),
    path('recovery',x.recoveryover),
    path('logout' , views.login),
    path('register' , views.register)
]