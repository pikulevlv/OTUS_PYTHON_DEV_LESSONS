from collections import namedtuple
from dataclasses import dataclass

@dataclass(frozen=False) #если Ложь, можем менять объекты
class User:
    id: int
    username: str
    is_staff: bool= False

u = User(id=1, username='john')
admin = User(id=42, username='admin', is_staff=True)

print("user", u)
print("admin", admin)
print(admin.is_staff)

