# обычный класс
# class Food:
#
#     def __init__(self, name, food_type):
#         self.name = name
#         self.food_type = food_type

# датакласс
from dataclasses import dataclass

# удобно для создания простых классов
# т.к. сразу реализует методы __init__, __repr__, сравнения
@dataclass(frozen=True) #froqen=True чтобы класс стал неизменяемым (не получится после создания поменять имя еды)
class Food:
    name: str
    food_type: str

if __name__ == '__main__':
    food = Food('Honey', 'Sweet')
    print(food)

    food1 = Food('Honey', 'Sweet')

    print('food == food1', food == food1)
    # food1.name = 'Fat'

    # food2 = Food('Smth', 2)
    # print(type(food2.food_type))