from django.shortcuts import render
from accounts.forms import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from business.views import *

def home(request):
    return render(request,'accounts/home.html')
def index(request):
    return render(request,'accounts/index.html')
@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return render(request, 'accounts/home.html')
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(initial={'username':  'Enter Username', 'password':'Enter Password'},data=request.POST)
        
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'accounts/registration.html',
                          {'user_form':user_form,
                            'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            User.objects.get(username=username)
        except:
            return render(request, 'accounts/login.html' , {'login_error': 'User not found!'})
        user = authenticate(username=username, password=password)
        if user and user.is_authenticated:
            login(request,user)
            return render(request, 'business/home.html')
        else:
            return HttpResponse("Your account was inactive.")
    else:
        return render(request, 'accounts/login.html', {})