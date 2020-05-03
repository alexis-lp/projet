from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=300)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name
