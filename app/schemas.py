# remote-brick/schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional, Dict

class User(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class LinkID(BaseModel):
    user_id: str
    linked_id: Optional[str] = None

class UserDetails(BaseModel):
    user_id: str
    address: Optional[str] = None
    phone: Optional[str] = None
    preferences: Optional[Dict] = None
