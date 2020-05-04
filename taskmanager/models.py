from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=300)
    members = models.ManyToManyField(User)

    class Meta:
        verbose_name = 'projet'
    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name='statut'

    def __str__(self):
        return self.name

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

class Journal(models.Model):
    date = models.DateTimeField()
    entry = models.CharField(max_length=100)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    task = models.ForeignKey(Task,on_delete=models.CASCADE)

    class Meta:
        verbose_name= 'journal'

    def __str__(self):
        return "Commentaire du {0}".format(self.date)

