from fastapi import FastAPI
from pydantic import BaseModel

#2:38:00 Hay codigo que hcie aparte pero da el mismo output, el metodo post si sirve


app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [
    User(id=1, name="Johan", surname="Carvajal", url="https://havertzz.netlify.app/", age=26),
    User(id=2, name="Laura", surname="Martínez", url="https://lauramartinez.dev/", age=25),
    User(id=3, name="Carlos", surname="Ramírez", url="https://carloscodes.io/", age=32),
    User(id=4, name="Andrea", surname="Gómez", url="https://andreagomez.com/", age=27),
    User(id=5, name="David", surname="Fernández", url="https://davidfz.netlify.app/", age=30)
]

@app.get("/users")
async def get_users():
    return users_list


@app.get("/user/{id}")
async def get_user(id: int):
    user = search_user(id)
    if user:
        return user
    return {"error": "User not found"}


@app.post("/user")
async def create_user(user: User):
    if search_user(user.id):
        return {"error": "User already exists"}
    users_list.append(user)
    return user


def search_user(id: int):
    for user in users_list:
        if user.id == id:
            return user
    return None
