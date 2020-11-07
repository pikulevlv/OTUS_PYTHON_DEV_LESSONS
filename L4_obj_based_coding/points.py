class Point:
    IS_2D = True
    all_instances = []
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = None
        self.all_instances.append(self)
    def __str__(self):
        # print(self.__class__)
        return f"{self.__class__.__name__} (x={self.x}, y={self.y})"
    def __repr__(self):
        return str(self)
    def move_up(self):
        self.y += 1

    @classmethod
    def copy(cls, from_point):
        return cls(from_point.x, from_point.y)
    def copy_me(self):
        return self.__class__(self.x, self.y)
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z



class AnotherPoint(Point):
    # ap_instances = []
    all_instances = []



print(Point.all_instances)
p = Point(4,5)
print(Point.all_instances)
print("point z", p.z)
print(p.IS_2D)
print(Point.IS_2D)
print(type(Point))
print(Point.__mro__) # показывает наследование
print(type(p)) # показывает наследование
print(type(type))
print(p.__class__.__name__)
print(type(lambda x: x))
print(type(Point.__init__))
# p.x = 0
# p.y = 0
# p2 = Point()
p2 = p
p.x += 1
p2.y -= 1
print(p, p2, p is p2)
p3 = p2.copy(p)
print(p3, p2, p3 is p2, p3 is p)
print('p3 == p', p3 == p)

p4 = p3 + p
print('p4', p4)
p4 = p2.copy_me
print(p4, p2, p4 is p2, p4 is p)

print(p, p.x, p.y)
print("move up")
print(p.move_up(), p)
print(Point.move_up(p))

Point(1,2)
print(Point.all_instances)
print("Another", AnotherPoint.all_instances)

print()
print()
print()
print()

def my_func():
    """
    docstring
    :return:
    """
    pass
my_func.extra_value = 123
print(my_func.__name__, my_func.__doc__, my_func.extra_value)

def _get_conn(*args):
    print("Creating conn", args)
    return ...

def get_connection(*args):
    if get_connection._conn is None:
        get_connection._conn = _get_conn(*args)
    return get_connection._conn
get_connection._conn = None

conn1 = get_connection()
conn2 = get_connection()
print(conn1 is conn2)
pi = 3.1415926
print(f"{pi:.3f}")
print('{:.3f}'.format(pi, 'g'))

print(isinstance(type, object))
print(isinstance(1, object))
print(isinstance(print(), object))