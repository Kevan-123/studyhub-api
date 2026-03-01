from rest_framework import serializers
from .models import StudyGoal

class StudyGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyGoal
        fields = '__all__'
        read_only_fields = ['user']