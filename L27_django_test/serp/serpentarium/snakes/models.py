from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Основные типы полей
# Int
# models.IntegerField()
# models.PositiveIntegerField()
# models.PositiveSmallIntegerField()
# Boolean
# models.BooleanField()
# Text
# models.TextField()
# Array (связь)
# Datetime, time, date
# models.DateTimeField
# models.DateField
# models.TimeField
# jsonb
# models.JSONField
# Float
# models.FloatField
# models.DecimalField
# Url, Email
# models.URLField
# models.UUIDField
# bites, blob
# models.BinaryField
# Картинка
# models.ImageField()
# models.FileField()


class Family(models.Model):
    "Семейство"
    name = models.CharField(max_length=128, unique=True)
    def __str__(self):
        return self.name

class Specia(models.Model):
    "Вид"
    name = models.CharField(max_length=128)
    family = models.ForeignKey(Family, on_delete=models.PROTECT, null=True)
    unique_together = [['name', 'family']]
    # poison
    is_poison = models.BooleanField(default=True)
    # food
    food = models.ManyToManyField("Food", blank=True)
    image = models.ImageField(upload_to='kind', blank=True, null=True)

    def __str__(self):
        return self.name

    def snake_count(self):
        result = Snake.objects.filter(specia=self).count()
        return result

class Food(models.Model):
    name = models.CharField(max_length=128, unique=True)
    def __str__(self):
        return self.name

class SnakeCard(models.Model):
    text = models.TextField(null=True)
    examplare = models.OneToOneField("Snake", on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'card #{self.id} ({self.examplare})'

class Snake(models.Model):
    # name
    name = models.CharField(max_length=128)
    card = models.OneToOneField(SnakeCard, on_delete=models.SET_NULL, blank=True, null=True)
    specia = models.ForeignKey(Specia, on_delete=models.PROTECT, default='')

    # age
    age = models.PositiveIntegerField(blank=True, null=True)
    file = models.FileField(upload_to='snake_examples', blank=True, null=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

# class SnakeSpeciaImage(models.Model):
#     """Если понадобится несколько картинок на 1 вид змей"""
#     image = models.ImageField(upload_to='snakes')
#     specia = models.ForeignKey(Specia, on_delete=models.CASCADE)
