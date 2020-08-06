from django.shortcuts import render
from django.contrib.auth.models import User
from . forms import UserForm
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from placement.models import *
from django.contrib import messages
from personal.models import *


# Create your views here.
@login_required(login_url="/login/")
def dashboard(request):
    context = {}
    context['user'] = request.user
    return render(request, 'dashboard.html', context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))

def user_profile(request):
    return render(request, 'student/profile.html')

def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            context["error"] = "Your username or password is incorrect!"
            return render(request, "login.html", context)
    else:
        return render(request, "login.html", context)

def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()            
            return render(request, 'dashboard.html')
        else:
            return render(request, 'add.html', {"user_form": user_form})
    else:
        user_form = UserForm()
        return render(request, 'add.html', {"user_form": user_form})