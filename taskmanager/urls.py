from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('connexion',views.connexion,name='connexion'),
    path('deconnexion',views.deconnexion,name='deconnexion'),
    path('projects',views.projects, name='list_projects'),
    path('project/<int:id_du_projet>',views.project,name='Contenu du projet'),
]