from django.shortcuts import render, get_object_or_404, redirect
from todo.models import Task
from todo.form import TaskText

def todo(request):
    templates = "todo/todo.html"
    todolist = Task.objects.filter(user_id=request.user.id)
    form = TaskText()
    context = {
        "todolist":todolist,
        "form":form
    }
    return render(request, templates, context)

def todo_del(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect("todo:todo")

def todo_add(request, complexity):
    form = TaskText(request.POST)
    if form.is_valid():
        task = form.save(commit=False)
        task.user_id = request.user
        task.complexity = complexity
        task.save()
        return redirect("todo:todo")

def complate_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.T_or_F = not task.T_or_F
    task.save()
    return redirect("todo:todo")
