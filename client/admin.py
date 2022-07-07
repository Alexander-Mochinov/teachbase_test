from django.contrib import admin

from client.models import (
    User,
    AuthorizationData,
)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Пользователь"""
    pass

@admin.register(AuthorizationData)
class AuthorizationDataAdmin(admin.ModelAdmin):
    """Данные авторизации"""
    pass
