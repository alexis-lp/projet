from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('connexion',views.connexion,name='connexion'),
    path('deconnexion',views.deconnexion,name='deconnexion'),
    path('projects',views.projects, name='list_projects'),
    path('project/<int:id_du_projet>',views.project,name='Contenu du projet'),
    path('project/<int:id_du_projet>/task/<int:id_task>',views.task,name="Journal de la tâche"),
    path('project/<int:id_du_projet>/newtask',views.newtask,name="Création d'une tâche"),

]