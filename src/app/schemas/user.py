# src/app/schemas/user.py

from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserRead(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    username: str
    password: str
