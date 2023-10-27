from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from src import crud, models, schemas

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


# Test 1: test_main::test_health
@app.get("/health")
def health():
    raise HTTPException(status_code=404, detail="Not Healthy")

# Test 2: test_main::test_get_users
@app.get("/people", response_model=list[schemas.User])
def read_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users

# Test 3: test_main::test_get_items
@app.post("/items", response_model=list[schemas.Item])
def read_items(db: Session = Depends(get_db)):
    items = crud.get_items(db)
    return items
