from django.db import models

class Snake(models.Model):
    # name
    name = models.CharField(max_length=100)
    # age
    age = models.PositiveIntegerField(null=True)
    # poison
    is_poison = models.BooleanField(default=True)
    # food
    food = models.TextField(null=True)

    def __str__(self):
        return self.name