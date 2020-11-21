from django.core.management.base import BaseCommand
from snakes.models import Family, Specia, Food, SnakeCard, Snake


class Command(BaseCommand):
    help = 'Work with db'

    def handle(self, *args, **options):
        print('Hello from command')
        # # Удаление
        # Food.objects.all().delete()
        # Animal.objects.all().delete()
        # Kind.objects.all().delete()
        SnakeCard.objects.all().delete()
        Snake.objects.all().delete()
        Specia.objects.all().delete()
        Family.objects.all().delete()
        Food.objects.all().delete()

        #Creation
        snake_family = Family.objects.create(name='Vulgaris') # save without need commit
        snake_food_1 = Food.objects.create(name='spiders')
        snake_food_2 = Food.objects.create(name='insects')
        snake_specia = Specia.objects.create(name='Cobra', family=snake_family, is_poison=False)
        snake_specia.food.add(snake_food_1)
        snake_specia.food.add(snake_food_2)
        snake_example_1 = Snake.objects.create(name='Vanda', specia=snake_specia)
        snake_example_2 = Snake.objects.create(name='Liza', specia=snake_specia)

        #Updating
        print(snake_example_1, snake_example_2)
        # snake_example.name = 'VANDA'
        snake_example_1.save() #для одного объекта нужно делать сейв
        snake_example_2.save() #для одного объекта нужно делать сейв
        print(snake_example_1, snake_example_2)
        print("id", snake_example_1.id)
        print("card", snake_example_1.card)
        print("spec", snake_example_1.specia)
        print("age", snake_example_1.age)
        print("food", snake_example_1.specia.food.all())
        print("poison", snake_example_1.specia.is_poison)

        # # 3 основных типа запроса
        # # 1. Выборка всех данных
        snakes = Snake.objects.all()

        for snake in snakes:
            print(f'- {snake.name}')
        # # 2. Выборка 1-го объекта
        snake = Snake.objects.get(name='Vanda')
        print(type(snake))
        print(snake.id)

        # # 3. Выборка нескольких объектов (фильтрация)
        snakes = Snake.objects.filter(specia=snake_specia)
        # # Вернется QuerySet - несколько найденных объектов
        for snake in snakes:
            print(snake.name)

