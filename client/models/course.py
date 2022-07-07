from django.db import models

from client.models import (
    User,
    Author,
    Type,
)


class Course(models.Model):
    """Модель курса"""

    name = models.CharField(
        verbose_name="Название курса",
        null=False,
        blank=True,
        max_length=64,
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now_add=True,
        null=True,
        blank=True,
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата обновления",
        null=True,
        blank=True,
    )
    content_type = models.PositiveIntegerField(
        verbose_name="Номет объекта",
        null=True,
        blank=True,
    )
    owner_name = models.CharField(
        verbose_name="ФИО владельца",
        null=True,
        blank=True,
        max_length=64,
    )
    thumb_url = models.CharField(
        verbose_name="thumb_url",
        null=True,
        blank=True,
        max_length=64,
    )
    cover_url = models.CharField(
        verbose_name="cover_url",
        null=True,
        blank=True,
        max_length=64,
    )
    description = models.TextField(
        verbose_name="Описание",
        null=True,
        blank=True,
    )
    last_activity = models.DateTimeField(
        verbose_name="Последняя активность",
        null=True,
        blank=True,
    )
    total_score = models.PositiveIntegerField(
        verbose_name="Общий счёт",
        null=True,
        blank=True,
    )
    total_tasks = models.PositiveIntegerField(
        verbose_name="Всего задач",
        null=True,
        blank=True,
    )
    is_netology = models.BooleanField(
        verbose_name="Нетология",
        default=False,
    )
    bg_url = models.CharField(
        verbose_name="bg_url",
        null=True,
        blank=True,
        max_length=64,
    )
    video_url = models.CharField(
        verbose_name="video_url",
        null=True,
        blank=True,
        max_length=64,
    )
    demo = models.BooleanField(
        verbose_name="Демо версия",
        default=False,
    )
    unchangeable = models.BooleanField(
        verbose_name="Неизменный",
        default=False,
    )
    include_weekly_report = models.BooleanField(
        verbose_name="Исключить недельный отчёт",
        default=False,
    )
    custom_author_names = models.CharField(
        verbose_name="Пользовательские имена авторов",
        null=True,
        blank=True,
        max_length=64,
    )
    custom_contents_link = models.CharField(
        verbose_name="Настраиваемое содержимое",
        null=True,
        blank=True,
        max_length=255,
    )
    hide_viewer_navigation = models.BooleanField(
        verbose_name="Нетология",
        default=False,
    )
    duration = models.PositiveIntegerField(
        verbose_name="Продолжительность",
        null=True,
        blank=True,
    )
    account = models.ForeignKey(
        User,
        verbose_name="Аккаунт",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    authors = models.ManyToManyField(
        Author,
        verbose_name="Авторы",
        blank=True,
    )
    types = models.ManyToManyField(
        Type,
        verbose_name="Типы",
        blank=True,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "cource"
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
