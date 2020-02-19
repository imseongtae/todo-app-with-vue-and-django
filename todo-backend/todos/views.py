from django.shortcuts import render
from .models import Todo
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

# Create your views here.

def todo_list(request):
  todos = Todo.objects.all() # 리스트로 다 가져옴
  todo_list = []
  for todo in todos:
    context_text = {"id": todo.id, "todo": todo.todo, "create": todo.create_date}
    todo_list.append(context_text)

  return JsonResponse(todo_list, safe=False)

@csrf_exempt
def todo_api(request):
  if request.method == 'GET':
    return todo_list(request)
  elif request.method == 'POST':
    return create_todo(request)

def create_todo(request):
  todo = Todo()
  todo.todo = json.loads(request.body).get('todo')
  todo.save()
  return JsonResponse({"result": todo.id}, safe=False)


@csrf_exempt
@require_http_methods(['DELETE'])
def remove_todo(request, id):
  todo = Todo.objects.get(pk=id)
  if todo:
    todo.delete()
    return JsonResponse({"result": "OK"}, safe=False)
  else:
    return JsonResponse({"result": "FAIL"}, safe=False)


@csrf_exempt
def todo_remove_all(request):
  todos = Todo.objects.all()
  for todo in todos:
    todo.delete()

  return JsonResponse({"result": "OK"}, safe=False)