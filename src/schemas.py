from pydantic import BaseModel


class Item(BaseModel):
    title: str
    description: str | None = None
    owner_id: int



class User(BaseModel):
    name: str
    email: str
    items: list[Item] = []

    
