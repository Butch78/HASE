from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int



class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    
