from fastapi import FastAPI, Depends, Request
from sqlalchemy.orm import Session
import pydantic
from typing import List
from enternal import database, models, schemas, crud

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/get_users")
async def get_users(request: Request, db: Session = Depends(get_db)):
    result = crud.get_users(db)
    return result


@app.post("/create_user", response_model=schemas.User)
async def create_user(instance: schemas.CreateUser, db: Session = Depends(get_db)):
    result = crud.create_user(db, instance=instance)
    return result