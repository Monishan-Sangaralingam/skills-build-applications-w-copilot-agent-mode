from rest_framework import viewsets
from .models import User, Team, Activity, Workout, Leaderboard
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, WorkoutSerializer, LeaderboardSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings

CODESPACE_URL = "https://fantastic-space-computing-machine-g4jr5w6wg7xf94wp-8000.app.github.dev"
LOCAL_URL = "http://localhost:8000"

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

@api_view(['GET'])
def api_root(request, format=None):
    # Return both codespace and local URLs for endpoints
    return Response({
        'users': {
            'codespace': f'{CODESPACE_URL}/api/users/',
            'local': f'{LOCAL_URL}/api/users/'
        },
        'teams': {
            'codespace': f'{CODESPACE_URL}/api/teams/',
            'local': f'{LOCAL_URL}/api/teams/'
        },
        'activity': {
            'codespace': f'{CODESPACE_URL}/api/activity/',
            'local': f'{LOCAL_URL}/api/activity/'
        },
        'workouts': {
            'codespace': f'{CODESPACE_URL}/api/workouts/',
            'local': f'{LOCAL_URL}/api/workouts/'
        },
        'leaderboard': {
            'codespace': f'{CODESPACE_URL}/api/leaderboard/',
            'local': f'{LOCAL_URL}/api/leaderboard/'
        },
    })
