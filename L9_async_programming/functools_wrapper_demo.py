def another_function(func):
    """
    Функция которая принимает другую функцию
    """

    def wrapper():
        """
        Оберточная функция
        """
        val = "The result of %s is %s" % (func(),
                                          eval(func())
                                          )

        return val

    return wrapper


@another_function
def a_function():
    """Обычная функция"""
    return "1+1"


if __name__ == "__main__":
    print(a_function.__name__)
    print(a_function.__doc__)



from functools import wraps

def another_function(func):
    """
    Функция которая принимает другую функцию
    """

    @wraps(func)
    def wrapper():
        """
        Оберточная функция
        """
        val = "The result of %s is %s" % (func(), eval(func()))
        return val

    return wrapper


@another_function
def a_function():
    """Обычная функция"""
    return "1+1"


if __name__ == "__main__":
    # a_function()
    print(a_function.__name__)
    print(a_function.__doc__)
