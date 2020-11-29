from mixer.backend.django import mixer
from django.core.management.base import BaseCommand
from snakes.models import Family, Specia, Food, SnakeCard, Snake
# from datetime import datetime
from django.utils import timezone
import string


def delete_all():
    Snake.objects.all().delete()
    SnakeCard.objects.all().delete()
    Food.objects.all().delete()
    Specia.objects.all().delete()
    Family.objects.all().delete()

class Command(BaseCommand):

    def handle(self, *args, **options):
        # Очищаем базу
        delete_all()
        # Создаем случайную змею
        family = mixer.blend(Family) # сразу и в базу сохраняет
        print(family)

        # Создаем связанные объекты
        specia = mixer.blend(Specia)
        print(specia)
        print(specia.family.name)

        snakecard = mixer.blend(SnakeCard)
        print(snakecard)
        print(snakecard.examplare)

        # Задание полей
        snake = mixer.blend(Snake, specia=specia)
        print(snake)
        # print(snakecard.examplare)

        snakecard = mixer.blend(SnakeCard, examplare=snake)
        print(snakecard)
        print(snakecard.examplare)

        # Задание полей для связанной модели
        delete_all()
        specia = mixer.blend(Specia, family__name='Super Family')
        print(f'List attrs of {specia}')
        for key in specia.__dict__:
            print(f'{key}:', specia.__dict__[key])
        print('family name:', specia.family.name)
        print('-/'*10)

        delete_all()
        snake = mixer.blend(Snake, specia__name='Some specia', specia__family__name='Some Family')
        print(snake)
        print(snake.specia)
        print(snake.specia.family.name)
        print('-/'*10)

        # Выбор из списка значений
        delete_all()
        family = mixer.blend(Family, name=mixer.RANDOM('Family A', 'Family B', 'Family C'))
        print(family.name)

        # с распаковкой имен из списка
        delete_all()
        names = ['Family A', 'Family B', 'Family C']
        family = mixer.blend(Family, name=mixer.RANDOM(*names))
        print(family.name)

        # Задание поля на основе уже данного
        delete_all()
        # specia = mixer.blend(Specia)
        # snake = mixer.blend(Snake, specia=specia)
        snake = mixer.blend(Snake, specia__id=100)
        # snakecard = mixer.blend(SnakeCard, examplare=snake,
        #                     some_date=datetime.now(), create_month=mixer.MIX.some_date.month)
        snakecard = mixer.blend(SnakeCard, examplare=snake,
                            some_date=timezone.now(), create_month=mixer.MIX.some_date.month)
        print(snakecard.create_month)
        print(snakecard.some_date)

        print('-/'*10)
        # Создание нескольких записей
        delete_all()
        names = ['Family A', 'Family B', 'Family C']
        families = mixer.cycle(3).blend(Family)
        print(families)
        for i in families:
            print('id:', i.id, i.name)

        # последовательности
        names = ['Family A', 'Family B', 'Family C']
        families = mixer.cycle(3).blend(Family, name=mixer.sequence(*names))
        print(families)
        for i in families:
            print('id:', i.id, i.name)

        # последовательности
        delete_all()
        num = 3
        alphabet = string.ascii_uppercase
        names = list(alphabet[:num])
        f_names = list(map(lambda i: f'Family {i}', names))
        families = mixer.cycle(num).blend(Family,
                                        name=mixer.sequence(*f_names))
        print(families)
        for i in families:
            print('id:', i.id, i.name)


        print('Done!')