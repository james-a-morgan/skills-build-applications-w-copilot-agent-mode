from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', members=['Iron Man', 'Captain America', 'Thor', 'Hulk'])
        dc = Team.objects.create(name='DC', members=['Superman', 'Batman', 'Wonder Woman', 'Flash'])

        # Create users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='Marvel', superpower='Genius, Suit'),
            User(email='captain@marvel.com', name='Captain America', team='Marvel', superpower='Super Soldier'),
            User(email='thor@marvel.com', name='Thor', team='Marvel', superpower='God of Thunder'),
            User(email='hulk@marvel.com', name='Hulk', team='Marvel', superpower='Strength'),
            User(email='superman@dc.com', name='Superman', team='DC', superpower='Flight, Strength'),
            User(email='batman@dc.com', name='Batman', team='DC', superpower='Detective, Gadgets'),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='DC', superpower='Amazonian'),
            User(email='flash@dc.com', name='Flash', team='DC', superpower='Speed'),
        ]
        User.objects.bulk_create(users)

        # Create activities
        activities = [
            Activity(user='Iron Man', activity_type='Running', duration=30, date='2026-02-20'),
            Activity(user='Superman', activity_type='Flying', duration=60, date='2026-02-20'),
            Activity(user='Batman', activity_type='Training', duration=45, date='2026-02-20'),
            Activity(user='Thor', activity_type='Weightlifting', duration=50, date='2026-02-20'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=120)
        Leaderboard.objects.create(team='DC', points=110)

        # Create workouts
        workouts = [
            Workout(name='Hero HIIT', description='High intensity interval training for heroes.', suggested_for='Marvel'),
            Workout(name='Speed Run', description='Running workout for speedsters.', suggested_for='DC'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
