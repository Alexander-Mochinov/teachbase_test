from django.db import models
from django.forms import model_to_dict
from django.core.validators import RegexValidator
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager as Manager


class UserManager(Manager):
    pass


class User(AbstractBaseUser, PermissionsMixin):
    """Расширенный пользователь"""

    class LangsChoice(models.TextChoices):
        """Языки"""

        ru = "ru", "ru"
        eng = "eng", "eng"

    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$", 
        message="Phone number must be entered in the format.",
    )

    email = models.EmailField(
        verbose_name="Email", 
        unique=True, 
        null=True, 
        blank=True,
    )
    first_name = models.CharField(
        verbose_name="Имя", 
        max_length=25, 
        unique=True, 
        null=True, 
        blank=True,
    )
    second_name = models.CharField(
        verbose_name="Фамилия", 
        max_length=25, 
        unique=True, 
        null=True,
        blank=True,
    )
    patronymic = models.CharField(
        verbose_name="Отчество", 
        max_length=25, 
        unique=True, 
        null=True, 
        blank=True,
    )
    is_active = models.BooleanField(
        verbose_name="Статус активности", 
        default=True,
    )
    username = models.CharField(
        verbose_name="Пользователь", 
        max_length=25, 
        unique=True, 
        null=True, 
        blank=True,
    )
    date_of_birth = models.DateField(
        verbose_name="Дата рождения", 
        blank=True, 
        null=True,
    )
    date_joined = models.DateTimeField(
        verbose_name="Дата регистрации", 
        auto_now_add=True,
    )
    hide_personal_data = models.BooleanField(
        verbose_name="Скрыть персональные данные:", 
        default=False, 
        blank=True,
    )
    phone = models.CharField(
        verbose_name="Мобильный номер телефона", 
        validators=[phone_regex], 
        max_length=17, 
        blank=True,
    )
    is_staff = models.BooleanField(
        verbose_name="Является ли сотрудником", 
        default=False,
    )
    is_supervisor = models.BooleanField(
        verbose_name="Является ли руководителем", 
        default=False,
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата обновления", 
        null=True, 
        blank=True,
    )
    lang = models.CharField(
        verbose_name="Язык", 
        choices=LangsChoice.choices, 
        default=LangsChoice.ru, 
        max_length=5,
    )


    objects = UserManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    def to_json(self):
        return model_to_dict(self)

    def has_permission(self, perm):
        """Проверка прав пользователя на совершения действия"""

        if self.is_active and self.is_superuser:
            return True

        return perm in self.user_permissions.all()
        
    __repr__ = __str__

    class Meta:
        db_table = "user"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
