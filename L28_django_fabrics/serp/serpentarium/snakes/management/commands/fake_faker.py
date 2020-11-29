from django.core.management.base import BaseCommand
# from snakes.models import Family, Specia, Food, SnakeCard, Snake
from faker import Faker

class Command(BaseCommand):

    def handle(self, *args, **options):
        faker = Faker()
        name = faker.name()
        text = faker.text()
        word = faker.word()
        phone = faker.phone_number()
        color = faker.color(hue='red', color_format='rgb')
        code = faker.country_calling_code()
        print(name)
        print(text)
        print(word)
        print(phone)
        print(color)
        print(code)
        print('Done!')