from fastapi import FastAPI
from routers import users, basic_auth_users
from fastapi.staticfiles import StaticFiles

#4:40:35 IMPORTANT, he explained all the code made with OAuth2

app = FastAPI()

app.include_router(users.router)
app.include_router(basic_auth_users.router)

#app.mount("/static", StaticFiles(directory="static"), name="logo") traer archivos estaticos

