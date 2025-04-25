from django.urls import path
from . import views
from .views import TaskDetailView

urlpatterns = [
    path('api/', views.tasks, name='task_list_create'),
    path('api/<int:task_id>/', views.tasks, name='task_detail'),
    path('api/filter/date/', views.filter_tasks_by_date, name='filter_by_date'),
    path('api/filter/urgency/', views.filter_tasks_by_urgency, name='filter_by_urgency'),
    path('api/filter/tag/', views.filter_tasks_by_tag, name='filter_by_tag'),
    path('tags/', views.TagListView.as_view(), name='tag_list'),
    path('urgency-levels/', views.UrgencyListView.as_view(), name='urgency_list'),
]
