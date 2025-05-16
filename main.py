from fastapi import FastAPI
from data.users import users_list
from models.user import User
from utils.user_search import search_user

app = FastAPI()

@app.get("/users")
async def get_users():
    return users_list


@app.get("/user/{id}")
async def get_user(id: int):
    user = search_user(id)
    if user:
        return user
    

@app.post("/user")
async def create_user(user: User):
    if search_user(user.id):
        return {"error": "User already exists"}
    users_list.append(user)
    return user


@app.put("/user")
async def update_user(user: User):
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            return user
    return {"error": "User not found"}


@app.delete("/user/{id}")
async def delete_user(id: int):
    for index, deleted_user in enumerate(users_list):
        if deleted_user.id == id:
            del users_list[index]
            return {"message": "The user has been deleted"}
    return {"error": "User not found"}
        