import traceback # для  полного вывода исключения
# Способы импортов
#1. Весь модуль
# import animals # в коде пишем animals.class_name
#2. Весь модуль с псевдонимом
# import animals as am # в коде пишем am.class_name
#3. конкретно то, что нужно
# from animals import Bear, PositiveValueError
#4. Все - не рекомендую
# from animals import *
#5. импорт модуля, который еще в папке (папках)
# from core.subcore.animals import Bear, PositiveValueError
#6. Модули и пакеты
# from corepackage.animals import Bear, PositiveValueError
from corepackage import Bear, PositiveValueError # если в __init__ прописаны эти импорты, то можно и так

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