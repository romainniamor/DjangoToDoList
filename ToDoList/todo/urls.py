
from django.urls import path
from . import views
from .views import *


app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    path('tasks', views.tasks, name='tasks'),
    path('tasklist', TaskList.as_view(), name='tasklist'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create_task/', TaskCreate.as_view(), name='task_create'),
    path('task_update/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('task_confirm_delete/<int:pk>/', TaskDelete.as_view(), name='task_delete'),

    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='todo:index'), name='logout'),
    path('register/', Register.as_view(), name='register'),
]