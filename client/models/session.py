from tabnanny import verbose
from django.db import models

from client.models import (
    Course,
    Label,
)


class Session(models.Model):
    """Модель сессии курса"""

    class AccessType(models.TextChoices):
        privy = "privy", "Привватный"
        publy = "publy", "Публичный"

    name = models.CharField(
        verbose_name="Название типа",
        null=False,
        blank=True,
        max_length=255,
    )
    started_at = models.DateTimeField(
        verbose_name="Дата начала",
        auto_now_add=True,
    )
    finished_at = models.DateTimeField(
        verbose_name="Дата окончания",
        auto_now_add=True,
    )
    infinitely = models.BooleanField(
        verbose_name="Повторяющая сессия",
        default=False,
    )
    access_type = models.CharField(
        verbose_name="Тип доступа",
        choices=AccessType.choices,
        default=AccessType.privy,
        max_length=32,
    )
    finished = models.BooleanField(
        verbose_name="Закончилась сессия",
        default=False,
    )
    navigation = models.PositiveIntegerField(
        verbose_name="Навигация",
        null=True,
        blank=True,
    )
    apply_url = models.CharField(
        verbose_name="Применяемый URL",
        max_length=1024,
        null=True,
        blank=True,
    )
    deadline_soon =  models.BooleanField(
        verbose_name="Дедлайн скоро",
        default=False,
    )
    assignments_count = models.PositiveIntegerField(
        verbose_name="Cчетчик заданий",
        null=True,
        blank=True,
    )
    deadline_type = models.PositiveIntegerField(
        verbose_name="ID типа дедлайна",
        null=True,
        blank=True,
    )
    slug = models.CharField(
        verbose_name="Ссыдка на курс",
        max_length=255,
        null=True,
        blank=True,
    )
    period = models.DateTimeField(
        verbose_name="Дата окончания",
        auto_now_add=True,
    )
    course = models.ForeignKey(
        Course,
        verbose_name="Курс",
        on_delete=models.CASCADE,
    )
    labels = models.ManyToManyField(
        Label,
        verbose_name="Теги/Заголовки",
        blank=True,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "session"
        verbose_name = "Сессия"
        verbose_name = "Сессии"
