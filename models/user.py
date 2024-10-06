from pydantic import BaseModel
from typing import Optional



class User(BaseModel):
    name: str
    email: str
    password: str
    role: Optional[str] = None


class LoginRequest(BaseModel):
    email: str
    password: str