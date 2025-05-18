from fastapi import FastAPI
from routers import jwt_auth_users, users
from fastapi.staticfiles import StaticFiles

#4:40:35 IMPORTANT, he explained all the code made with OAuth2
#4:54:24 min video

app = FastAPI()

app.include_router(users.router)
app.include_router(jwt_auth_users.router)

#app.mount("/static", StaticFiles(directory="static"), name="logo") traer archivos estaticos

