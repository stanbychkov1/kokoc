from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    balance = models.PositiveIntegerField(default=0, verbose_name='Баланс')
    background_color = models.CharField(max_length=255, default='white',
                                        verbose_name='Цвет фона')
    username_color = models.CharField(max_length=255, default='black',
                                      verbose_name='Цвет логина')
    passed_test_quantity = models.PositiveIntegerField(
        default=0, verbose_name='Пройденные тесты')
    email = models.EmailField(verbose_name='E-mail',
                              unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
