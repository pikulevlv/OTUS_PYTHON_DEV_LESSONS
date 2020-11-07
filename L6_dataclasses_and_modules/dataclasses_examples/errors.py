class PositiveValueError(ValueError):

    def __init__(self, value, *args):
        self.value = value
    def __str__(self): # важно переопределить __str__
        return f'Age cant be below 0. You entered {self.value}'