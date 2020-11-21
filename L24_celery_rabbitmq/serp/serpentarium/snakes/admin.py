from django.contrib import admin

from .models import Snake, Family, Specia, Food, SnakeCard

# Register your models here.
admin.site.register(Snake)
admin.site.register(Family)
admin.site.register(Specia)
admin.site.register(Food)
admin.site.register(SnakeCard)