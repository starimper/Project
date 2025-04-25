from rest_framework import serializers
from .models import Task, Date, UrgencyLevel, Tag

class DateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    date = serializers.DateField()

class UrgencyLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrgencyLevel
        fields = ['id', 'name', 'color']

class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'date', 'urgency', 'tags', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def create(self, validated_data):
        tags = validated_data.pop('tags', [])
        task = Task.objects.create(user=self.context['request'].user, **validated_data)
        task.tags.set(tags)
        return task

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        if tags is not None:
            instance.tags.set(tags)

        return instance