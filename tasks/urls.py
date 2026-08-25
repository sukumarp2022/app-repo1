from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='list'),
    path('tasks/<int:pk>/toggle/', views.toggle_task, name='toggle'),
]