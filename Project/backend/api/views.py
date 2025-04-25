from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, generics, permissions 
from .models import Task, Date, UrgencyLevel, Tag

from .serializers import (
    TaskSerializer, DateSerializer, 
    UrgencyLevelSerializer, TagSerializer
)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def tasks(request, task_id=None):
    if request.method == 'GET':
        if task_id:
            task = Task.objects.filter(id=task_id, user=request.user).first()
            if task:
                serializer = TaskSerializer(task)
                return Response(serializer.data)
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        tasks = Task.objects.filter(user=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        if task_id:
            task = Task.objects.filter(id=task_id, user=request.user).first()
            if not task:
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = TaskSerializer(task, data=request.data, partial=False)  
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail": "Task ID is required."}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        if task_id:
            task = Task.objects.filter(id=task_id, user=request.user).first()
            if not task:
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = TaskSerializer(task, data=request.data, partial=True) 
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail": "Task ID is required."}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if task_id:
            task = Task.objects.filter(id=task_id, user=request.user).first()
            if not task:
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
            task.delete()
            return Response({"detail": "Task deleted."}, status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Task ID is required."}, status=status.HTTP_400_BAD_REQUEST)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def filter_tasks_by_date(request):
    filter_type = request.query_params.get('filter', 'closest') 
    if filter_type == 'closest':
        tasks = Task.objects.filter(user=request.user).order_by('date__date') 
    else:
        tasks = Task.objects.filter(user=request.user).order_by('-date__date') 
    
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def filter_tasks_by_urgency(request):
    filter_type = request.query_params.get('filter', 'most')  
    if filter_type == 'most':
        tasks = Task.objects.filter(user=request.user).order_by('-urgency__id')  
    else:
        tasks = Task.objects.filter(user=request.user).order_by('urgency__id')
    
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def filter_tasks_by_tag(request):
    tag_name = request.query_params.get('tag')  
    if tag_name:
        tasks = Task.objects.filter(user=request.user, tags__name=tag_name)  
    else:
        tasks = Task.objects.filter(user=request.user)  
    
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

class TagListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

class UrgencyListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        urgencies = UrgencyLevel.objects.all()
        serializer = UrgencyLevelSerializer(urgencies, many=True)
        return Response(serializer.data)