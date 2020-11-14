from django.core.management.base import BaseCommand
from animals.models import Family, Animal, Kind, Food


class Command(BaseCommand):
    help = 'Work with db'

    def handle(self, *args, **options):
        # Удаление
        Food.objects.all().delete()
        Animal.objects.all().delete()
        Kind.objects.all().delete()
        Family.objects.all().delete()
        # Создание
        family = Family.objects.create(name='Попугай')
        kind = Kind.objects.create(name='Бурый', family=family)
        Animal.objects.create(name='Борис', kind=kind)
        animal = Animal.objects.create(name='Миша', kind=kind)
        # Обновление
        family.name = 'Медведь'
        family.save()

        print(family.name)
        print(family.id)

        # Many To Many
        print(animal.foods)

        ham = Food.objects.create(name='Мясо')

        animal.foods.add(ham)
        honey = Food.objects.create(name='Мёд')
        animal.foods.add(honey)
        animal.save()

        print(animal.foods.all())

        # 3 основных типа запроса
        # 1. Выборка всех данных
        animals = Animal.objects.all()

        for animal in animals:
            print(animal.name)

        # 2. Выборка 1-го объекта
        animal = Animal.objects.get(name='Борис')
        print(type(animal))

        print(animal.id)

        # 3. Выборка нескольких объектов (фильтрация)
        #animals = Animal.objects.filter(name='Борис')
        animals = Animal.objects.filter(foods__in=[ham, honey])
        # Вернется QuerySet - несколько найденных объектов
        for animal in animals:
            print('food')
            print(animal.name)

        print('done')
