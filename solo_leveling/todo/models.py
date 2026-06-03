from django.db import models
from django.contrib.auth import get_user_model


class Task(models.Model):
    user_id = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    text = models.TextField(
        "Задача"
    )
    T_or_F = models.BooleanField(
        "Выполнена или нет",
        default=False
    )
    complexity = models.IntegerField(
        "Сложность",
        null=True,
    )

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
