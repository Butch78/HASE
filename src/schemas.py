from pydantic import BaseModel


class Item(BaseModel):
    title: str
    description: str | None = None
    owner_id: int


class UserCreate(BaseModel):
    name: str
    email: str
    

class User(UserCreate):
    name: str
    email: str
    items: list[Item] = []

    
