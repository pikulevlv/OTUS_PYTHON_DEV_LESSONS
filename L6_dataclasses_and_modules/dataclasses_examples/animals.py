from errors import PositiveValueError
from dataclasses import dataclass, field
from food import Food
from typing import Optional, Union, List, Tuple

# class Bear:
#     def __init__(self, name, age, food):
#         self.name = name
#         self.food = food
#         if age < 0:
#             # exception 1 - generation
#             # raise Exception('Age cant be below 0')
#             # raise ValueError('Age cant be below 0')
#             raise PositiveValueError(age) # передаем в исключение параметр!
#         self.age = age
#
#     def __str__(self):
#         return f"{self.name} {self.age}"
@dataclass
class Bear:
    name: str
    age: int
    # age: Union[int]
    food: Food
    feature: List[int] = field(default_factory=list)

    def __post_init__(self):
        self.name = f"Super {self.name}!"
        if self.age < 0:
            raise PositiveValueError(self.age) # передаем в исключение параметр!
        # if not isinstance(self.age, int):
        #     print('Ошибка значения')
        #     raise ValueError
        

# print('Имя класса Bear:',Bear.__name__)
# print('Имя всего модуля:', __name__)
#!!! выполнится только в самом модуле тут, но не там, где мы делаем импорт
if __name__ == '__main__':
    # print('I am from animals')
    food = Food('Honey', 'Sweet')
    bear = Bear('Faust', 5, food)
    print(bear)

# name = 'Faust'
# age = int(input('Enter age:'))

# Processing of exception
# try:
#     bear = Bear(name, age)
#     # 5/0
# except PositiveValueError as e:
#     # there was an error
#     print('there was an error', traceback.format_exc()) # для  полного вывода исключения
# except ValueError as e:
#     print('Value error', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError!')
# except Exception:
#     print('Smth went on wrong way')
# else:
#     # there wasn't an error
#     print('Bear instance is done')
#     print(bear)
# finally:
#     # it must be execute anyway
#     print('the end')
