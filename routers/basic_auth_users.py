from fastapi import APIRouter, HTTPException, Depends, status
from models.models import Register, RegisterDB
from data.db import users_db
from utils.utils import search_register_user
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter(prefix="/users_db", tags=["Users Autentication"])
oauth2 =OAuth2PasswordBearer(tokenUrl="login")


async def current_user(token: str = Depends(oauth2)):
    user = search_register_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credencials",
            headers={"WWW-Authenticate": "Bearer"}
        )
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Deactivated user"
        )
    return user


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400, detail="The username is not correct")

    user = search_register_user(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=400, detail="Incorrect password")
    
    return {"access_token": user.username, "token_type": "bearer"}
        

@router.get("/me")
async def me(user: Register = Depends(current_user)):
    return user