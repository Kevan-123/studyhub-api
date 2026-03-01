from django.db import models
from goals.models import StudyGoal

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class LearningResource(models.Model):
    goal = models.ForeignKey(StudyGoal, on_delete=models.CASCADE, related_name='resources')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    link = models.URLField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title