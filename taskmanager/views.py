from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


# Create your views here.


def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)

            if user and user.is_active:
                login(request, user)
                return redirect(reverse('list_projects'))
            else:
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'taskmanager/connexion.html', locals())

def deconnexion(request):
    logout(request)
    return redirect(reverse('connexion'))

def projects(request):
    user_projects = Project.objects.filter(members=request.user)
    return render(request,'taskmanager/projects.html',locals())

