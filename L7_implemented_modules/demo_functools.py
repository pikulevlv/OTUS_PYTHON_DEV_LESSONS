from functools import wraps
from functools import partial # позволяет передать функции не все аргументы
from functools import lru_cache #

power_of_2 = lambda x: pow(x, 2)
print(power_of_2(2))
print(power_of_2(3))
print('-'*15)
p2 = partial(pow, exp=2) #функция, арги и кварги
print(p2(3))
print(p2(4))
print(p2(5))
print('-'*15)
p = partial(pow, 3) # как если бы мы вызвали pow(3, ...), т.е. еще не знаем второй аргумент
print(p(1)) # pow(3, 1)
print(p(2)) # pow(3, 2)
print(p(3)) # pow(3, 3)
print('-'*15)

def fib(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print('долго без lru_cache')
print([fib(n) for n in range(33)]) # долго без lru_cache

print("Используем декоратор trace, чтобы увидеть ход вычислений")
def trace(func):
    func.level = 0
    @wraps(func)
    def inner(*args, **kwargs):
        print('____' * func.level + ' --> {}({})'.format(func.__name__, args[0]))
        func.level += 1
        f = func(*args, **kwargs)
        func.level -= 1
        print('____' * func.level + ' <-- {}({}) == {}'.format(func.__name__, args[0], f))
        return f
    return inner

@trace
def fib(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print([fib(n) for n in range(5)])

@lru_cache(maxsize=2048) # можно увеличить с 1024 до нужного значения
@trace
def fib(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print("быстро с lru_cache и trace")
print([fib(n) for n in range(33)]) # быстро с lru_cache

# своя реализация lru_cache
def my_lru_cache(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        try:
            return cache[args]
        except KeyError:
            pass
        res = func(*args)
        cache[args] = res
        return res
    return wrapper

@my_lru_cache
@trace
def fib(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print("быстро с самописным lru_cache и trace")
print([fib(n) for n in range(33)]) # быстро без lru_cache
