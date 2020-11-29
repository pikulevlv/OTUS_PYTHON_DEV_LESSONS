import math
from mixer.backend.django import mixer
from django.test import TestCase, Client
# from unittest import TestCase as utc
from .models import Specia, Family, Snake
from django.contrib.auth.models import User


# Create your tests here.
class TestExample(TestCase):
    """Example class"""

    def test_pi_r(self):
        self.assertEqual(round(math.pi, 2), 3.14)
    # def test_pi(self):
    #     self.assertEqual(math.pi, 3.14)


class TestSpecia(TestCase):
    """Testing Models"""

    def setUp(self):
        """
        Сюда помещаем все, что нужно для теста
        """
        # print('I launch myself and clean test base before every test')
        # self.snake_family_name = Family.objects.create(name='Family_For_All')
        # self.snake_family_name = mixer.blend(Family, name='Family_For_All')
        self.snake_specia_name = 'Snake_For_All'


        # self.specia_1 = Specia.objects.create(
        #     name=self.snake_specia_name,
        #     family=self.snake_family_name,
        # )
        self.specia_1 = mixer.blend(Specia, name=self.snake_specia_name)

        self.snake_name_1 = 'Varga'

        # self.specia_2 = Specia.objects.create(
        #     name=self.snake_specia_name,
        #     family=self.snake_family_name,
        # )
        self.specia_2 = mixer.blend(Specia, name=self.snake_specia_name)


    def tearDown(self):
        """
        Тут удаляем все, что нужно почистить
        """
        # print('I launch myself after every test')
        return

    def test_str(self):
        # print(f"Сравниваем строчное представление "
        #       f"экземляра класса '{type(self.specia_1)}' с именем '{self.snake_specia_name}' "
        #       f"и строку '{self.snake_specia_name}'")
        self.assertEqual(str(self.specia_1), self.snake_specia_name)

    def test_unique(self):
        # print(self.specia_1.name)
        self.assertEquals(self.specia_1.name, self.specia_2.name)

    def test_snake_specia_count(self, num=3):
        self.assertEqual(self.specia_1.snake_count(), 0)

        # snake_name_1 = 'Vanda'
        # snake_1 = Snake.objects.create(
        #     name=snake_name_1,
        #     specia=self.specia_1,
        # )
        snake_1 = mixer.cycle(num).blend(Snake, specia=self.specia_1)
        self.assertEqual(self.specia_1.snake_count(), num)

    # Что желательно проверить в models
    # 1. 100% методов классов
    # 2. Проверка создаваемых инстансов

class TestViews(TestCase):
    """Testing Views with Client without launching server"""
    def setUp(self):
        self.client = Client()
        # self.snake_family_name = Family.objects.create(name='Family_For_All')
        self.snake_family_name = mixer.blend(Family, name='Family_For_All')
        self.snake_specia_name = 'Snake_For_All'
        # self.specia_1 = Specia.objects.create(
        #     name=self.snake_specia_name,
        #     family=self.snake_family_name,
        # )
        self.specia_1 = mixer.blend(Specia, name=self.snake_specia_name,
                                      family=self.snake_family_name)
        self.snake_name_1 = 'Varga'
        # self.snake = Snake.objects.create(
        #     name=self.snake_name_1,
        #     specia=self.specia_1
        # )
        self.snake = mixer.blend(Snake, name=self.snake_name_1,
                                 specia=self.specia_1)

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.status_code, 201)
        encoding = 'utf-8'
        text = response.content.decode(encoding)
        searched = '<button type="submit" class="btn btn-primary">Save and send</button>'
        # check if buttons exist in the page
        self.assertTrue(searched in text)
        # print(response.context)
        self.assertTrue('object_list' in response.context.keys())
        self.assertTrue('active_page' in response.context.keys())
        self.assertEqual(response.context['active_page'], "1")


    # Что желательно проверить в views
    # 1. status code для разных пользователей
    # 2. Проверка создаваемых из форм объектов
    # 3. Контекст

    def test_permissions(self):
        # авторизация пользователя
        admin = User.objects.create_superuser('admin', 'test@test.com', '12345678qwerty')
        staff = User.objects.create_user('staff', 'staff@test.com', '12345678qwerty', is_staff=True)
        user = User.objects.create_user('user', 'user@test.com', '12345678qwerty', is_staff=False)
        # snake/<int:pk>/delete/
        url = f'/snake/{self.snake.id}/delete/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

        # for admin
        self.client.login(username='admin', password='12345678qwerty')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.client.logout()

        # for staff
        self.client.login(username='staff', password='12345678qwerty')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

        url = '/create/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.client.logout()

        # for user
        self.client.login(username='user', password='12345678qwerty')
        url = '/create/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)
        self.client.logout()

