
from rest_framework import serializers
from .models import Task, TaskStatus, Category
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = '__all__'

class CategorySimpleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)

class UserSimpleSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=150)
