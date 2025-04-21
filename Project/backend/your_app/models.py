
from django.db import models
from django.contrib.auth.models import User

class TaskStatus(models.Model):
    name = models.CharField(max_length=50)

class Category(models.Model):
    title = models.CharField(max_length=100)

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    importance = models.IntegerField(default=1)
    status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
