from fastapi import FastAPI,exceptions, Query, Header, Depends
from demo_pydantic import User, UserBase, UserOut
from typing import Optional, Dict

app = FastAPI()

ids = iter(range(1, 10_000_000))

USERS = {}

USER_BY_TOKEN: Dict[str, User] = {}

@app.get("/")
def hello_world(name: Optional[str] = Query(default="world")):
    """
    ## Returns greeting
    1. is json
    1. is documented
    1. greets the world
    :return:
    """
    return {"message": f"Hello {name}!"}

@app.get("/{item_id}/")
def item(item_id: int):
    """
    Returns item id
    :param item_id:
    :return:
    """
    return {"item_id": item_id}



# принимаем запрос
@app.post("/user/", response_model=UserOut,
          tags=["User"])
def create_user(user_in: UserBase): # UserBase нужна только для валидации
    user = User(id=next(ids), **user_in.dict()) # создаем пользователя
    USERS[user.id] = user
    USER_BY_TOKEN[user.token] = user
    return {"user": user.dict()} #возвращаем данные юзера

def get_current_user(token: str = Header(...), description="user auth token (user_id") -> User:
    if token not in USER_BY_TOKEN:
        raise exceptions.HTTPException(404, f"user token {token!r} not found")
    user = USER_BY_TOKEN[token]
    return user

@app.get("/user/me/",response_model=User, tags=["User"])
def get_me(user: User = Depends(get_current_user)):
    return user

@app.get("/user/{id}/", response_model=User, tags=['User'])
def get_user(id: int):
    """
    Returns user if found
    :param id:
    :return:
    """
    try:
        user = USERS[id]
    except KeyError:
        raise exceptions.HTTPException(404, f"user {id} not found")
    return user.dict()