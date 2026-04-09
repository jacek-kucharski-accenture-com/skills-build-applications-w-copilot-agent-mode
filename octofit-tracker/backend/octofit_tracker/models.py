from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class Team(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    team = models.ForeignKey('Team', null=True, blank=True, on_delete=models.SET_NULL)

class Activity(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    duration = models.IntegerField()

class Leaderboard(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    score = models.IntegerField()

class Workout(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
