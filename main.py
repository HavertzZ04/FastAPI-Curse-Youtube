from fastapi import FastAPI, HTTPException
from data.users import users_list
from models.user import User
from utils.user_search import search_user

app = FastAPI()

@app.get("/users", response_model=list[User])
async def get_users():
    return users_list


@app.get("/user/{id}", response_model=User)
async def get_user(id: int):
    user = search_user(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
    

@app.post("/user", response_model=User, status_code=201)
async def create_user(user: User):
    if search_user(user.id):
        raise HTTPException(status_code=409, detail="User already exists")
    users_list.append(user)
    return user


@app.put("/user", response_model=User)
async def update_user(user: User):
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/user/{id}", status_code=200)
async def delete_user(id: int):
    for index, deleted_user in enumerate(users_list):
        if deleted_user.id == id:
            del users_list[index]
            return {"message": "The user has been deleted"}
    raise HTTPException(status_code=404, detail="User not found")
        