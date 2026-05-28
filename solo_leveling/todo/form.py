from django import forms
from todo.models import Task


class TaskText(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["text"]