from django.shortcuts import render
from todo.models import Task

def todo(request):
    templates = "todo/todo.html"
    todolist = Task.objects.filter(user_id=request.user.id)
    context = {
        "todolist":todolist
    }
    return render(request, templates, context)
