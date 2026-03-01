from rest_framework import serializers
from .models import StudyGoal
from .models import Task


class StudyGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyGoal
        fields = '__all__'
        read_only_fields = ['user']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['goal']  # assigned via view if needed