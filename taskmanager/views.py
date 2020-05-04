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

def project(request,id_du_projet):
    project = Project.objects.get(pk=id_du_projet)
    tasks = Task.objects.filter(project=projet)
    return render(request,'taskmanager/project.html',locals())


def task(request,id_du_projet,id_task):
    task = Task.objects.get(pk=id_task)
    journal = Journal.objects.filter(task=task)
    return render(request,'taskmanager/task.html',locals())

def newtask(request,id_du_projet):
    error = False
    project = Project.objects.get(pk=id_du_projet)
    form = TaskForm(request.POST or None)

    if form.is_valid():
        task = form.save(commit=False)
        task.project = project
        user_assigned = task.assignee
        if user_assigned in project.members:
            task.save()
            return redirect(reverse('Journal de la tâche', args=[project.id, task.id]))
        else:
            error = True

    return render(request,'taskmanager/newtask.html',locals())