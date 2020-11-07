# import my_module
# print(my_module.MY_VARIABLE)
# from lesson.my_module import MY_VARIABLE
# print(MY_VARIABLE)

# class Foo:
#     """My Foo class"""
#     bar = True
#
#     def echo(self):
#         print(self.__class__.__name__)
#     # @classmethod # тогда метод принимает не инстанс, а сам класс
#     # def echo_name(cls):
#     #     print(cls.__name__)
#
#     @staticmethod # позволяет определить метод класса, который ничего не принимает
#     def echo_name(cls):
#         print(Foo.__name__)

# class FooNew(Foo):
#     pass

def print_class_demo(klass):
    f = klass()
    print(klass, klass.__class__, type(klass))
    print(f, f.__class__, type(f))

    print("Class:", klass.echo_name())
    print("Instance:", f.echo_bar())
    print(klass.bar, f.bar)

    f.bar = False
    print(klass.bar, f.bar)

    f.bar = True
    klass.bar = False
    f2 = klass()
    f2.echo_bar()
    print(klass.bar, f.bar, f2.bar)

@classmethod
def echo_name(cls):
    print(cls.__name__)
def echo_bar(self):
    print(self.bar)

# можно создавать классы через type(). Это полезно, когда в программе надо сгенерировать класс находу
# Foo = type('Foo', (), {'bar':True, 'echo_name':echo_name, 'echo_bar':echo_bar})
# NewFoo = type('NewFoo', (Foo, ), {'spam':'eggs'})
#
# print(Foo)
#
# print(NewFoo)
# nf = NewFoo()
# print(nf)
# print(nf.spam)



class MyMetaclass(type):
    def __new__(cls, name, bases, dct, *args, **kwargs):
        # print('New class', name)
        # print('Bases', bases)
        dct['SPAM'] = 'EGGS'
        # print('New attrs', dct)

        # for k in dct.keys():
        #     if k.startswith('_'):
        #         v = dct.pop(k)
        #         dct[k.upper()] = v

        undrs = [k for k in dct.keys() if k.startswith('_')]
        for undr in undrs:
            dct[undr.upper()] = dct[undr]
            del dct[undr]

        new_cls = super().__new__(cls, name, bases, dct, *args, **kwargs)
        # print("Created new cls", new_cls)
        return new_cls

# Foo = MyMetaclass('Foo', (), {})
#
# NewFoo = MyMetaclass('NewFoo', (Foo,), {'spam':'eggs'})

# print('Creating new Foo class')
class Foo(metaclass=MyMetaclass):

    def __new__(cls, *args, **kwargs):
        print('__new__ Foo', cls)
        bar = True
        _secret_attr = 'secret value'

    @classmethod
    def echo_name(cls):
        print(cls.__name__)
    def echo_bar(self):
        print(self.bar)
print("Created new Foo class")

class NewFoo(Foo):
    spam = 'eggs'
    class SubNewCls:
        new = False

# print(NewFoo.SubNewCls.new)

# print(Foo.SPAM)
# print(NewFoo.SPAM)
# f = Foo()
# nf = NewFoo()
# print(f, f.SPAM)
# print(nf, nf.SPAM)
#
# # print_class_demo(Foo)
# print(Foo._SECRET_ATTR)

from abc import ABCMeta, abstractmethod
class FileManagerABC(metaclass=ABCMeta):
    @abstractmethod # все абстрактные методы должны быть реализованы в классе-наследнике
    def read_file(self) -> str:
        raise NotImplementedError
    @abstractmethod
    def write_to_file(self, text: str) -> int:
        """
        Write to file
        :param text:
        :return:
        """
    # @abstractmethod
    # def close(self) -> None:
    #     """
    #     Closing file
    #     :return:
    #     """


class FileManager(FileManagerABC):
    def __init__(self, filename: str):
        # self._f = open(filename, 'r+')
        self._filename = filename
    def read_file(self) -> str:
        with open(self._filename, 'r') as f:
            text = f.read()
            # self.f.seek(0) # возвращает каретку в начало файла
            return text
    def write_to_file(self, text: str) -> int:
        with open(self._filename, 'a') as f:
            count = f.write(text)
            print('written text', text)
            return count

    # def close(self) -> None:
    #     print("closing", self.f)
    #     self.f.close()

file_manager = FileManager('file.txt')
print(file_manager.read_file())
print(file_manager.write_to_file('\nhello again!'))
