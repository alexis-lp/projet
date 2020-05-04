from django import forms
from .models import *

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        exclude = ('project',)




