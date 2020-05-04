from django import forms
from .models import *

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur",
                               max_length=30,
                               widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label="Mot de passe",
                               widget=forms.PasswordInput(attrs={'class':'form-control'}))


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        exclude = ('project',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['assignee'].widget.attrs.update({'class': 'form-control'})
        self.fields['start_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['due_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['priority'].widget.attrs.update({'class': 'form-control'})
        self.fields['status'].widget.attrs.update({'class': 'form-control'})






