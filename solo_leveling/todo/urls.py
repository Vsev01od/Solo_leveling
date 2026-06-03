from django.urls import path
from todo import views

app_name = "todo"

urlpatterns = [
    path("", views.todo, name="todo"),
    path("del/<int:id>/", views.todo_del, name="todo_del"),
    path("add/<int:complexity>/", views.todo_add, name="todo_add"),
    path("complate_task/<int:id>/", views.complate_task, name="complate_task"),
]
