from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from uuid import uuid4


class UserBase(BaseModel):
    username: str
    is_staff: bool= False
    date_banned: Optional[datetime] = None

    class Config:
        # extra = Extra.ignore
        extra = 'forbid' # не позволит передать в USer левые аргументы

def generate_token() -> str:
    token = str(uuid4())
    print("new token", token)
    return token

class User(UserBase):
    id: int
    token: str = Field(default_factory=generate_token)

    # class Config:
    #     orm_mode = True # если объект алхимии

def create_user(username: Optional[str] = None):
    """

    :param username:
    :return:
    """
    if username is None:
        username = 'qwerty'
    return User(id=0,username=username)

u = create_user(123)




class UserOut(BaseModel):
    user: User



if __name__ == '__main__':

    u = User(id=1, username='john')
    admin = User(id=42, username='admin', is_staff=True)

    print("user", repr(u))
    print("admin", repr(admin))
    print(admin.is_staff)

    user_data = {
        "id": 1,
        "username": "user",
        # "is_admin": True
    }

    u2 = User(**user_data)

    print(repr(u2))

    user_dict = u2.dict(exclude_unset=False)
    print('Return all attrs')
    print(user_dict)

    user_dict = u2.dict(exclude_unset=True)
    print('Return obviously set attrs')
    print(user_dict)

    # user_dict = u2.dict(exclude=set('id'))
    user_dict = u2.dict(exclude={'id'})
    print('Return attrs except excluded')
    print(user_dict)