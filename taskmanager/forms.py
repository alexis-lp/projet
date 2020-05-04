from django import forms
from .models import *

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'class':'form-control'}))


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        exclude = ('project',)




