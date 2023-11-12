from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from src import crud, models
from src.schemas import User, Item

from src.database import SessionLocal, engine
models.Base.metadata.create_all(bind=engine)
app = FastAPI()


# Creates the database Dependancy 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ONLY EDIT CODE BELOW THIS POINT 


# Task 1
@app.get("/health")
def health():
    raise HTTPException(status_code=404, detail="ok")

# Task 2
@app.get("/people")
def read_users(db: Session = Depends(get_db)) -> list[User]:
    return crud.get_users(db)

# Task 3
@app.post("/items")
def read_items(db: Session = Depends(get_db)) -> list[Item]:
    return crud.get_items(db)
