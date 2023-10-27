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


# Task 1: Test Get Health
@app.get("/health")
def health():
    raise HTTPException(status_code=404, detail="Not Healthy")


# Task 2: Test Get Users
@app.get("/people")
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)


# Tasl 3: Test Get Items
@app.post("/items")
def read_items(db: Session = Depends(get_db)):
    return crud.get_items(db)
