from django.db import models
from django.contrib.auth.models import User

class Date(models.Model):
    date = models.DateField(unique=True)

    def __str__(self):
        return self.date.isoformat()

class UrgencyLevel(models.Model):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'
    URGENCY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]

    name = models.CharField(max_length=10, choices=URGENCY_CHOICES, unique=True)
    color = models.CharField(max_length=7, help_text='HEX code for display, e.g. #FF0000')

    def __str__(self):
        return self.get_name_display()

class Tag(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tags')

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date = models.ForeignKey(Date, on_delete=models.CASCADE, related_name='tasks')
    urgency = models.ForeignKey(UrgencyLevel, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    tags = models.ManyToManyField(Tag, blank=True, related_name='tasks')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date', 'urgency']

    def __str__(self):
        return f"{self.title} ({self.date.date.isoformat()})"
