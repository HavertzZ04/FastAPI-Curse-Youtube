from fastapi import FastAPI
from routers import users

#3:33:13 min of the video

app = FastAPI()


app.include_router(users.router)
