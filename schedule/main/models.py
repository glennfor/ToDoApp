from turtle import ondrag
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AgendaList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="agendalist", null=True)
    name = models.CharField(max_length=200)

    def __str__(self,):
        return self.name

class ListItem(models.Model):
    agenda = models.ForeignKey(AgendaList, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    done = models.BooleanField()

    def __str__(self,):
        return self.text