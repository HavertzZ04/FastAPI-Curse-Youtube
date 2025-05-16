from data.users import users_list

def search_user(user_id: int):
    for user in users_list:
        if user.id == user_id:
            return user
    return None

    