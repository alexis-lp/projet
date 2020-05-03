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
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    description = models.TextField()
    assignee = models.ForeignKey(User,on_delete=models.PROTECT)
    start_date = models.DateField()
    due_date = models.DateField()
    priority = models.IntegerField()
    status = models.ForeignKey(Status,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'tâche'

    def __str__(self):
        return self.name