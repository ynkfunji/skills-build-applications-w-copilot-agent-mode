from django.contrib import admin
from django.contrib.auth.models import User
from .models import CustomUser, Team, Activity, Leaderboard, Workout, Exercise

# Avoid re-registering the User model

# Register other models
admin.site.register(CustomUser)
admin.site.register(Team)
admin.site.register(Activity)
admin.site.register(Leaderboard)
admin.site.register(Workout)
admin.site.register(Exercise)