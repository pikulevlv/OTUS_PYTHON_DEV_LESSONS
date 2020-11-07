import traceback # для  полного вывода исключения

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

# bear = Bear('Faust', 5)
# print(bear)
# bear = Bear('Faust', -5)
# print(bear)

name = 'Faust'
age = int(input('Enter age:'))

# Processing of exception
try:
    bear = Bear(name, age)
    # 5/0
except PositiveValueError as e:
    # there was an error
    print('there was an error', traceback.format_exc()) # для  полного вывода исключения
except ValueError as e:
    print('Value error', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError!')
except Exception:
    print('Smth went on wrong way')
else:
    # there wasn't an error
    print('Bear instance is done')
    print(bear)
finally:
    # it must be execute anyway
    print('the end')
#