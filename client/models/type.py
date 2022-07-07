from django.db import models


class Type(models.Model):
    """Модель типа курса"""

    name = models.CharField(
        verbose_name="Название типа",
        null=False,
        blank=True,
        max_length=255,
    )
    created_at = models.DateTimeField(
        verbose_name="Дата обновления",
        null=True,
        blank=True,
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата обновления",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "type_course"
        verbose_name = "Тип курса"
        verbose_name_plural = "Типы курсов"
