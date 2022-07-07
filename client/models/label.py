from django.db import models


class Label(models.Model):
    """Заголовок/Тег курса"""

    name = models.CharField(
        verbose_name="Название типа",
        null=False,
        blank=True,
        max_length=255,
    )
    created_at = models.DateTimeField(
        verbose_name="Дата обновления",
        auto_now_add=True,
        null=True,
        blank=True,
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата обновления",
        null=True,
        blank=True,
    )
    labels = models.ManyToManyField(
        "self", 
        verbose_name="Дочерние Заголовоки/Теги курса",
        blank=True,
    )

    def __str__(self) -> str:
        return f'{self.name}: {self.created_at}'

    class Meta:
        db_table = "lable"
        verbose_name = "Заголовок/Тег курса"
        verbose_name_plural = "Заголовоки/Теги курса"
