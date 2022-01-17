from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    image = models.ImageField(verbose_name='Фотография', upload_to='users_image', blank=True)
    department = models.CharField(verbose_name='Отдел', max_length=50)
    post = models.CharField(verbose_name='Должность', max_length=50)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
