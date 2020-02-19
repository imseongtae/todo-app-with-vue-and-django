from django.urls import path, include
from .views import *

urlpatterns = [
  path('todos/', todo_api, name="list"),
  path('todos/<int:id>/', remove_todo, name="update"),
  path('todos/removeAll', todo_remove_all, name="removeAll"),
]