from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import StudyGoal
from .serializers import StudyGoalSerializer
from .models import Category, LearningResource
from .serializers import CategorySerializer, LearningResourceSerializer

class StudyGoalViewSet(viewsets.ModelViewSet):
    serializer_class = StudyGoalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return StudyGoal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()  # optional: add admin-only later

class LearningResourceViewSet(viewsets.ModelViewSet):
    serializer_class = LearningResourceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return LearningResource.objects.filter(goal__user=self.request.user)