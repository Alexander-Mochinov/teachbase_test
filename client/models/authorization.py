from tabnanny import verbose
from django.db import models

from client.models import User


class AuthorizationData(models.Model):
    """Данные авторизации"""

    user = models.OneToOneField(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
    )
    access_token = models.CharField(
        verbose_name="Токен авторизации",
        null=False,
        blank=True,
        max_length=64,
    )
    token_type = models.CharField(
        verbose_name="Тип токена",
        null=False,
        blank=True,
        max_length=64,
    )
    expires_in =  models.TimeField(
        verbose_name="Истекает", 
        blank=True, 
        null=True
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания токена",
        auto_now_add=True,
        null=True,
        blank=True,
    )
    client_id = models.CharField(
        verbose_name="Публичный ключ",
        null=False,
        blank=True,
        max_length=64,
    )
    client_secret = models.CharField(
        verbose_name="Секретный ключ",
        null=False,
        blank=True,
        max_length=64,
    )
    grant_type = models.CharField(
        verbose_name="Тип гранта",
        null=False,
        blank=True,
        max_length=64,
        default="client_credentials",
    )
    resource_owner_id = models.CharField(
        verbose_name="Идентификатор владельца ресурса",
        null=True,
        blank=True,
        max_length=255,
    )

    def __str__(self) -> str:
        return f'Авторизация пользователя: {self.user}'

    class Meta:
        db_table = "authorization_data"
        verbose_name = "Данные авторизации"
        verbose_name_plural = "Данные авторизации"
