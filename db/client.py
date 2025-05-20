from models.models import User

users_list = [
    User(id=1, name="Johan", surname="Carvajal", age=26, country="Colombia"),
    User(id=2, name="Laura", surname="Martínez",  age=25, country="Brasil"),
    User(id=3, name="Carlos", surname="Ramírez",  age=32, country="Peru"),
    User(id=4, name="Andrea", surname="Gómez", age=27, country="Canada"),
    User(id=5, name="David", surname="Fernández", age=30, country="Argentina")
]


users_db = {
    "havertzz04": {
        "username": "havertzz04",
        "full_name": "Johan Carvajal",
        "email": "havertz2005@gmail.com",
        "disabled": False,
        "password": "$2y$10$XM3MyMwPH9M/V7r5UeDpguW5XKHPJR2S4/Z6eGXLrj8bN7hchQSfK"
    },
    "alexdev10": {
        "username": "alexdev10",
        "full_name": "Alejandro Pérez",
        "email": "alexdev10@gmail.com",
        "disabled": False,
        "password": "$2y$10$P5hCQUYqfjkCQ9YQJz0oX.sUPPyCurVuM89Zop.sdiJKY.CTzDaXW"
    },
}