from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

from .constants import (
    LENGTH_CHARFIELDS, LENGTH_EMAIL, USER_ROLES, LENGTH_PASSWORD, LENGTH_ROLES,
    UNIQUE_USERNAME, UNIQUE_EMAIL, USER, ADMIN
)
from .utils import (
    code_random, validate_username
)


class ApiUser(AbstractUser):
    username = models.CharField(
        'имя пользователя',
        max_length=LENGTH_CHARFIELDS,
        unique=True,
        validators=[validate_username],
        # Валидаторы поля username живут здесь)
        error_messages={
            'unique': (UNIQUE_USERNAME)
        }
    )
    email = models.EmailField(
        'почтовый адрес',
        max_length=LENGTH_EMAIL, unique=True,
        error_messages={
            'unique': (UNIQUE_EMAIL)
        }
    )
    first_name = models.CharField(
        'имя', max_length=LENGTH_CHARFIELDS, blank=True
    )
    last_name = models.CharField(
        'фамилия', max_length=LENGTH_CHARFIELDS, blank=True
    )
    bio = models.CharField(
        'описание', max_length=LENGTH_CHARFIELDS, blank=True, null=True)
    role = models.CharField(
        'роль', max_length=LENGTH_ROLES, blank=True,
        default=USER, choices=USER_ROLES
    )
    confirmation_code = models.SmallIntegerField('код', default=code_random())
    password = models.CharField(
        'пароль', max_length=LENGTH_PASSWORD, blank=True
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    def __str__(self):
        return self.username

    def save(self, **kwargs):
        self.set_api_permissions()
        super().save(**kwargs)

    def set_api_permissions(self):
        if self.is_superuser is True or self.user_is_admin:
            self.role = ADMIN
            self.is_staff = True
        else:
            self.is_staff = False

    @property
    def user_is_user(self):
        if self.role == USER:
            return True
        return False

    @property
    def user_is_admin(self):
        if self.role == ADMIN:
            return True
        return False

    @property
    def user_token(self):
        refresh = RefreshToken.for_user(self)
        return {
            'token': str(refresh.access_token),
        }
