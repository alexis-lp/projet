from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

"""
La fonction 
"""


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

@login_required
def projects(request):
    user_projects = Project.objects.filter(members=request.user)
    return render(request,'taskmanager/projects.html',locals())

@login_required
def project(request,id_du_projet):
    project = Project.objects.get(pk=id_du_projet)
    tasks = Task.objects.filter(project=project)
    return render(request,'taskmanager/project.html',locals())

@login_required
def task(request,id_du_projet,id_task):
    task = Task.objects.get(pk=id_task)
    journal = Journal.objects.filter(task=task)
    return render(request,'taskmanager/task.html',locals())

@login_required
def newtask(request,id_du_projet):
    error = False
    project = Project.objects.get(pk=id_du_projet)
    form = TaskForm(request.POST or None)

    if form.is_valid():
        task = form.save(commit=False)
        task.project = project
        user_assigned = task.assignee
        if user_assigned in project.members.all():
            task.save()
            return redirect(reverse('Journal de la tâche', args=[project.id, task.id]))
        else:
            error = True

    return render(request,'taskmanager/newtask.html',locals())

@login_required
def edittask(request,id_du_projet,id_task):
    error = False
    task = Task.objects.get(pk=id_task)
    project = Project.objects.get(pk=id_du_projet)

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            edit_task=form.save(commit=False)
            user_assigned = edit_task.assignee
            if user_assigned in project.members.all():
                edit_task.save()
                return redirect(reverse('Journal de la tâche', args=[project.id, task.id]))
            else:
                error = True
    else:
        form = TaskForm(instance=task)
    return render(request, 'taskmanager/edittask.html', locals())