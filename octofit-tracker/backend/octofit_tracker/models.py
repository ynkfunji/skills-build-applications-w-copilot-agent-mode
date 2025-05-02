from djongo import models
from django.contrib.auth.models import User

# Rename the custom User model to avoid conflicts
class CustomUser(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.JSONField()

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField()

class Workout(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    workout_type = models.CharField(max_length=50)
    date = models.DateField()

class Exercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    duration_minutes = models.IntegerField()
