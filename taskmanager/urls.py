from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('connexion',views.connexion,name='connexion'),
    path('deconnexion',views.deconnexion,name='deconnexion'),
    path('',views.home, name='home')
]