from fastapi import FastAPI
from routers import users
from fastapi.staticfiles import StaticFiles

#4:02:05 min of the video

app = FastAPI()

app.include_router(users.router)
app.mount("/static", StaticFiles(directory="static"), name="logo")
