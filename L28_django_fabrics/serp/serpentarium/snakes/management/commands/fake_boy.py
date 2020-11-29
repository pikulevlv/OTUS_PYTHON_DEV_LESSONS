from snakes.models import Family, Specia, Food, SnakeCard, Snake
from django.core.management.base import BaseCommand

import factory


class FamilyFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Family

    # name = 'Some Family'
    name = factory.Faker('name') # при помощи встроенного Faker

class CobraFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Family

    name = 'Cobra'

class UzhFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Family

    name = 'Uzh'

class SpeciaFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Specia

    # связанная модель
    family = factory.SubFactory(FamilyFactory)

    class Params:
        cobras = factory.Trait(
            name=factory.Iterator(['Poisonos', 'Bitesus', 'Black']),
            family=factory.SubFactory(CobraFactory)
        )
        uzhes = factory.Trait(
            name=factory.Iterator(['Vulgaris', 'Amobikus']),
            family=factory.SubFactory(UzhFactory)
        )


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
        # Простое создание модели
        family = FamilyFactory.create() # а метод build не сохраняет в базу
        print('name:', family.name, 'id:', family.pk)
        # Создание модели не в БД
        # family = FamilyFactory.build(name='Other Family') # задав name, переопределяем значение name
        family = FamilyFactory.build(name=factory.Faker('name')) # задав name, переопределяем значение name
        print('name:', family.name, 'id:', family.pk) # id не создается, это быстрее

        specia = SpeciaFactory.build(name=factory.Faker('name'))
        print('name:', specia.name, 'id:', specia.pk) # id не создается, это быстрее

        # Создание нескольких записей
        families = FamilyFactory.build_batch(5)
        # families = FamilyFactory.create_batch(5)
        for f in families:
            print(f.name, f.id)

        delete_all()
        families = FamilyFactory.create_batch(2, name=factory.Iterator(['Fam A', 'Fam B']))
        for f in families:
            print(f.name, f.id)

        delete_all()
        names = ['Fam A', 'Fam B']
        f_names = list(map(lambda i: f'family name: {i}', names))
        print(f_names)
        families = FamilyFactory.create_batch(2, name=factory.Iterator(f_names))
        for f in families:
            print(f.name, f.id)

        delete_all()
        names = ['Fam A', 'Fam B']
        f_names = list(map(lambda i: f'family name: {i}', names))
        print(f_names)
        families = FamilyFactory.create_batch(2, name=factory.Sequence(lambda i: f'name:{i}'))
        for f in families:
            print(f.name, f.id)

        #
        delete_all()
        species = SpeciaFactory.build_batch(3, cobras=True)
        print(species)
        for s in species:
            print(s.family.name, s.name, s.id)

        delete_all()
        species = SpeciaFactory.build_batch(2, uzhes=True)
        print(species)
        for s in species:
            print(s.family.name, s.name, s.id)