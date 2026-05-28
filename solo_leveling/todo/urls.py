from django.urls import path
from todo import views

app_name = "todo"

urlpatterns = [
    path("", views.todo, name="todo"),
    path("del/<int:id>/", views.todo_del, name="todo_del"),
    path("add/", views.todo_add, name="todo_add"),
]
