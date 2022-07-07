from django.db import models

from client.models import User


class Author(models.Model):
    """Модель автора"""

    users = models.OneToOneField(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f'{self.users.first_name or ""} {self.users.second_name or ""} {self.users.patronymic or ""}'


    class Meta:
        db_table = "author"
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
