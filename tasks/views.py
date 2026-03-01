from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import StudyGoal
from .serializers import StudyGoalSerializer
from .models import Task
from .serializers import TaskSerializer

class StudyGoalViewSet(viewsets.ModelViewSet):
    serializer_class = StudyGoalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return StudyGoal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return tasks for the current user’s goals
        return Task.objects.filter(goal__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save()  # expect goal id from POST