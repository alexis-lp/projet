from django.db import models
from django.contrib.auth.models import User

"""

La class 'Project' représente un projet.
Elle contient:
'name' une chaine de caractère contenant le nom du projet
'members' la liste des utilisateurs participants au projet

"""
class Project(models.Model):
    name = models.CharField(max_length=300)
    members = models.ManyToManyField(User)

    class Meta:
        verbose_name = 'projet'

    def __str__(self):
        return self.name

"""

La class 'Status' représente le status d'une tâche.
Elle contient:
'name' le nom du status


"""
class Status(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name='statut'

    def __str__(self):
        return self.name

"""

La class 'Task' représente une tâche.
Elle contient:
'project' le projet associé à la tâche
'name' le nom de la tâche
'description' une description de la tâche
'assignee' l'utilisateur associé à la tâche
'start_date' la date de début de la tâche
'due_date' la date limite de la tâche
'priority' le niveau de priorité de la tâche représenté par un entier
'status' le statut de la tâche

"""
class Task(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE,verbose_name="project")
    name = models.CharField(max_length=300,verbose_name="name")
    description = models.TextField(verbose_name="description")
    assignee = models.ForeignKey(User, on_delete=models.PROTECT,verbose_name="assignee")
    start_date = models.DateField(verbose_name="start date")
    due_date = models.DateField(verbose_name="due date")
    priority = models.IntegerField(verbose_name="priority")
    status = models.ForeignKey(Status,on_delete=models.CASCADE,verbose_name="status")

    class Meta:
        verbose_name = 'tâche'

    def __str__(self):
        return self.name

"""

La class 'Journal' représente le journal de commentaires sur une tâche.
Elle contient:

'date' la date du commentaire
'entry' le commentaire
'author' l'auteur du commentaire
'task' la tâche associée

"""
class Journal(models.Model):
    date = models.DateTimeField()
    entry = models.CharField(max_length=100)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    task = models.ForeignKey(Task,on_delete=models.CASCADE)

    class Meta:
        verbose_name= 'journal'

    # Dans l'administration, un commentaire sera défini par sa date de parution
    def __str__(self):
        return "Commentaire du {0}".format(self.date)

