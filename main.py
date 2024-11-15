from fastapi import FastAPI, Depends, Request
from sqlalchemy.orm import Session
from typing import List
from enternal import database, models, schemas, crud
import exceptions
import bcrypt
from tokens import token

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
    

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users/get_users")
async def get_users(db: Session = Depends(get_db)):
    result = crud.get_users(db)
    return result


@app.get("/users/get_user/{id}")
async def get_user(id: int, db: Session = Depends(get_db)):
    result = crud.get_user(db, id)
    if result is None:
        raise exceptions.UserNotFound()
    return result    


@app.post("/users/create_user", response_model=schemas.GetUser)
async def create_user(instance: schemas.CreateUser, db: Session = Depends(get_db)):
    result = crud.create_user(db, instance)
    return result

        
@app.post("/users/login")
async def login(instance: schemas.CreateUser, db: Session = Depends(get_db)):
    result = crud.login(db, instance)
    if result is None:
        raise exceptions.UserNotFound()
    # check_password = bcrypt.hashpw(instance.password.encode('utf-8'), bcrypt.gensalt())
    # print(instance.password,"\n\n\n", result.password)
    check_password = bcrypt.checkpw(instance.password.encode(), result.password)
    if not check_password:
        raise exceptions.InvalidPassword()
    return {'data': result, 'token': token.gen_token()}