from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    country: str
    
class Register(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool
    
class RegisterDB(Register):
    password: str