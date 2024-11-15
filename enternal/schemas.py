from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    password: str

class CreateUser(BaseModel):
    username: str
    password: str

class GetUser(BaseModel):
    id: int
    username: str