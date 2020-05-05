from django import forms
from .models import *
"""
La classe 'ConnexionForm' défini un formulaire de connexion
Ses attributs sont:
'username' l'identifiant de l'utilisateur, de longueur inférieure à 30 caractères
'password' le mot de passe de l'utilisateur
"""
class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur",
                               max_length=30,
                               #défini la mise en page à l'aide de bootstrap
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Mot de passe",
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


"""
La classe 'TaskFrom' défini un formulaire à partir du modèle Task
Ses attributs sont les attributs de Task excepté 'project'
"""
class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        exclude = ('project',)

    #Défini la mise en forme des champs à l'aide de Bootstrap
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['assignee'].widget.attrs.update({'class': 'form-control'})
        #Les dates doivent être retrées dans le format jj/mm/aaaa
        self.fields['start_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['due_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['priority'].widget.attrs.update({'class': 'form-control'})
        self.fields['status'].widget.attrs.update({'class': 'form-control'})






