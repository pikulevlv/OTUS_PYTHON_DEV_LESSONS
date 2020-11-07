from animals import Bear
from zoo import Zoo
from food import Food
from errors import PositiveValueError

food = Food('Honey', 'Sweet')
name = 'Faust'
# age = int(input('Enter age:'))
age = 3.5
feature = (3,)
bear = Bear(name, age, food, feature)
# zoo = Zoo([])
zoo = Zoo()
zoo.animals.append(bear)

print(zoo)
print(zoo.animals)