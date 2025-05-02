from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from octofit_tracker.models import Workout, Exercise
import random
from datetime import timedelta, datetime

class Command(BaseCommand):
    help = 'Populates the database with dummy users, workouts, and exercises'

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting database population...")

        # Optional: Clear existing data
        Exercise.objects.all().delete()
        Workout.objects.all().delete()

        # Clear existing data without using unsupported SQL operations
        for user in User.objects.all():
            if not user.is_superuser:
                user.delete()

        # Create users
        users = []
        for i in range(5):
            user = User.objects.create_user(
                username=f"user{i}",
                email=f"user{i}@example.com",
                password="password123"
            )
            users.append(user)

        self.stdout.write("Created 5 users")

        # Create workouts and exercises
        workout_types = ['Cardio', 'Strength', 'Yoga', 'HIIT']
        exercise_names = ['Push-up', 'Squat', 'Burpee', 'Jumping Jack', 'Plank']

        for user in users:
            for _ in range(3):  # 3 workouts per user
                workout = Workout.objects.create(
                    user=user,
                    workout_type=random.choice(workout_types),
                    date=datetime.now() - timedelta(days=random.randint(0, 30))
                )
                # Add exercises to the workout
                for _ in range(2):  # 2 exercises per workout
                    Exercise.objects.create(
                        workout=workout,
                        name=random.choice(exercise_names),
                        duration_minutes=random.randint(5, 30)
                    )

        self.stdout.write(self.style.SUCCESS("Database population complete."))
