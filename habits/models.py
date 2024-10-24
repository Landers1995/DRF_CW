from django.conf import settings
from django.db import models

NULLABLE = {"null": True, "blank": True}


class Habit(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Кто выполняет привычку",
        **NULLABLE,
    )
    location = models.CharField(
        max_length=200, default="Дома", verbose_name="Место выполнения привычки"
    )
    habit_time = models.DateTimeField(
        verbose_name="Дата и время выполнения привычки"
    )
    action = models.CharField(max_length=200, verbose_name="Выполняемое действие")
    is_nice = models.BooleanField(default=False, verbose_name="Приятноить привычка")
    related_habit = models.ForeignKey(
        "self", on_delete=models.SET_NULL, verbose_name="Связанность привычки", **NULLABLE
    )
    period = models.PositiveIntegerField(verbose_name="Период выполнения привычки")
    award = models.CharField(
        max_length=200, verbose_name="Вознаграждение", **NULLABLE
    )
    complete_time = models.DurationField(verbose_name="Время на выполнение привычки")
    is_public = models.BooleanField(default=True, verbose_name="Публичность привычки")

    def __str__(self):
        return f"{self.action}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
