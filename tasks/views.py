from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import StudyGoal
from .serializers import StudyGoalSerializer

class StudyGoalViewSet(viewsets.ModelViewSet):
    serializer_class = StudyGoalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return StudyGoal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)