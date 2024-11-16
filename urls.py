from django.urls import path
from .views import RegisterView, LoginView, TaskListView, TaskDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # Ensure this is correct
    path('login/', LoginView.as_view(), name='login'),
    path('task/', TaskListView.as_view(), name='task-list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]
