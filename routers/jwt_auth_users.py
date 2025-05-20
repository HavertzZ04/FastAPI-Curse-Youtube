from fastapi import APIRouter, HTTPException, Depends, status
from models.models import Register
from db.client import users_db
from utils.utils import search_register_user, search_register_user_db
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from jwt import PyJWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET_KEY = "61fa1e0f2cc87736590df115844042d75ab0c6ae01f58ac93556c4ea492bedc9"

router = APIRouter(prefix="/users_db", tags=["Users Autentication"])
oauth2 =OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])



async def auth_user(token: str = Depends(oauth2)):
    exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credencials",
            headers={"WWW-Authenticate": "Bearer"})  
    
    try:
        username = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM).get("sub")
        if username is None:
            raise exception
         
    except PyJWTError:
        raise exception 
    
    return search_register_user(username)

async def current_user(user: Register = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Deactivated user")
        
    return user


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400, detail="The username is not correct")
    user = search_register_user_db(form.username)
    
    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect password")
        
    access_token = {
        "sub": user.username,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_DURATION)
    }
    
    return {"access_token": jwt.encode(access_token, SECRET_KEY, algorithm=ALGORITHM), "token_type": "bearer"}
        

@router.get("/me")
async def me(user: Register = Depends(current_user)):
    return user