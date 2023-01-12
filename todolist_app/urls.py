from django.urls import path
from . import views


urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('delete/<task_id>', views.delete, name='delete'),
    path('complete/<task_id>', views.complete, name='complete'),
    path('pending/<task_id>', views.pending, name='pending'),
    path('edit/<task_id>', views.edit, name='edit'),
]


