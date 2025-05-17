from data.db import users_list, users_db
from models.models import RegisterDB


def search_user(user_id: int):
    for user in users_list:
        if user.id == user_id:
            return user
    return None


def search_register_user(username: str):
    if username in users_db:
        return RegisterDB(**users_db[username])
    