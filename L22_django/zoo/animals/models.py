from django.db import models


class Animal(models.Model):
    # кличка
    name = models.CharField(max_length=64)
    # возраст
    age = models.PositiveIntegerField()
    # тип - ?

    # что он есть - ?
    food = models.TextField()

    def __str__(self):
        return self.name

