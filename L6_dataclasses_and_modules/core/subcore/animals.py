class PositiveValueError(ValueError):

    def __init__(self, value, *args):
        self.value = value
    def __str__(self): # важно переопределить __str__
        return f'Age cant be below 0. You entered {self.value}'

class Bear:
    def __init__(self, name, age):
        self.name = name
        if age < 0:
            # exception 1 - generation
            # raise Exception('Age cant be below 0')
            # raise ValueError('Age cant be below 0')
            raise PositiveValueError(age) # передаем в исключение параметр!
        self.age = age
    def __str__(self):
        return f"{self.name} {self.age}"

print('Имя класса Bear:',Bear.__name__)
print('Имя всего модуля:', __name__)
#!!! выполнится только в самом модуле тут, но не там, где мы делаем импорт
if __name__ == '__main__':
    print('I am from animals')

