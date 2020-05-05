from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse



"""
La vue 'connexion' demande à l'utilisateur 
de s'authentifier pour accéder à ses projets.
C'est la première page qu'il verra.
"""
def connexion(request):
    #error = True signifie que les données rentrées dans le formulaire sont incorrectes
    error = False

    #Si le formulaire est rempli par l'utilisateur
    if request.method == "POST":
        form = ConnexionForm(request.POST)

        #Si le formulaire est correctement rempli"
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            #On vérifie que le pseudo et le mot de passe sont corrects
            user = authenticate(username=username, password=password)

            #Si les données sont correctes et que l'utilisateur est toujours actif
            if user and user.is_active:

                #On connecte l'utilisateur
                login(request, user)

                #On redirige l'utilisateur vers la liste de ses projets
                return redirect(reverse('list_projects'))

            #Le pseudo ou le mot de passe n'est pas bon
            else:
                error = True

    #Le form n'est pas encore rempli mais on le crée pour qu'il soit rempli
    else:
        form = ConnexionForm()

    return render(request, 'taskmanager/connexion.html', locals())


""" 
La vue 'deconnexion' déconnecte l'utilisateur
et le redirige vers la page connexion
"""
def deconnexion(request):
    logout(request)
    return redirect(reverse('connexion'))

"""
La vue 'projects' récupère tous les projets de l'utilisateur et
le dirige vers une page html où il pourra les retrouver
"""
#Demande la connexion de l'utilisateur pour autoriser l'acces à la page
@login_required
def projects(request):
    user_projects = Project.objects.filter(members=request.user)
    return render(request,'taskmanager/projects.html',locals())

"""
La vue 'project' prend en entrée l'identifiant du projet
et récupère toutes les tâches associées.
Elle envoie ensuite l'utilisateur vers une page html avec 
toutes les tâches associées au projet.
"""
@login_required
def project(request,id_du_projet):
    project = Project.objects.get(pk=id_du_projet)
    tasks = Task.objects.filter(project=project)
    return render(request,'taskmanager/project.html',locals())

"""
La vue 'task' prend en entrée l'identifiant du projet et de la tâche
puis récupère le journal d'activité associé à la tâche.
Elle envoie l'utilisateur vers une page ou il trouvera les détails de
sa tâche 
"""
@login_required
def task(request,id_du_projet,id_task):
    task = Task.objects.get(pk=id_task)
    journal = Journal.objects.filter(task=task)
    return render(request,'taskmanager/task.html',locals())


"""
La vue 'newtask' prend en entrée l'identifiant du projet dans lequel
on veut ajouter une tâche.
La vue crée un formulaire avec tous les champs que l'utilisateur
devra remplir.
Elle retourne une page html contenant le formulaire si ce dernier n'est
pas (ou pas correctement) rempli et la page de la nouvelle tâche crée sinon.
"""
@login_required
def newtask(request,id_du_projet):
    error = False
    project = Project.objects.get(pk=id_du_projet)
    #Crée un formulaire de type TaskForm
    form = TaskForm(request.POST or None)

    if form.is_valid():
        #crée une instance de task avec les données du formulaire mais ne la sauvegarde pas encore
        task = form.save(commit=False)
        task.project = project
        user_assigned = task.assignee

        #Verifie que l'utilisateur assigné à la tâche fait bien partie du projet
        if user_assigned in project.members.all():
            task.save()
            return redirect(reverse('Journal de la tâche', args=[project.id, task.id]))
        else:
            #L'utilisateur asssigné ne fait pas partie du projet
            error = True

    return render(request,'taskmanager/newtask.html',locals())

"""
La vue 'edittask' prend en entrée l'indentifiant du projet l'identifiant de la tâche à modifier
Elle renvoie une page html contenant un formulaire pré-rempli avec les données existantes sur la
tâche ou bien la page modifiée du journal.
"""

@login_required
def edittask(request,id_du_projet,id_task):
    error = False
    task = Task.objects.get(pk=id_task)
    project = Project.objects.get(pk=id_du_projet)

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            edit_task = form.save(commit=False)
            user_assigned = edit_task.assignee
            #Vérifie que l'utilisateur assigné est dans le projet
            if user_assigned in project.members.all():
                edit_task.save()
                return redirect(reverse('Journal de la tâche', args=[project.id, task.id]))
            else:
                error = True
    else:
        #Crée un formulaire de type TaskForm préremplis avec les données de 'task'
        form = TaskForm(instance=task)
    return render(request, 'taskmanager/edittask.html', locals())