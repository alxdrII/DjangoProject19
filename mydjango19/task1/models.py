from django.db import models
from django.contrib.auth.models import User


class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)  # Название
    cost = models.DecimalField(max_digits=15, decimal_places=2)  # Цена
    size = models.DecimalField(max_digits=15, decimal_places=0)  # Размер файлов
    description = models.TextField() # Описание
    age_limited = models.BooleanField(default=False) # Ограничение 18+
    buyer = models.ManyToManyField(Buyer)

    def __str__(self):
        return self.title
