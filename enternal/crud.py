from sqlalchemy.orm import Session
from sqlalchemy import select
from . import models, schemas
import bcrypt
from typing import List

def get_users(db: Session) -> List[models.User]:
    return db.query(models.User).all()
    

def get_user(db: Session, id: int) -> models.User | None:
    return db.query(models.User).get(id)
    
def create_user(db: Session, instance: schemas.CreateUser) -> models.User:
    hashed_password = bcrypt.hashpw(instance.password.encode('utf-8'), bcrypt.gensalt())
    model = models.User(username=instance.username, password=hashed_password)
    db.add(model)
    db.commit()
    return model

def login(db: Session, instance: schemas.CreateUser) -> models.User | None:
    stmt = select(models.User).where(models.User.username==instance.username)
    print(db.scalar(stmt), type(db.scalar(stmt)))
    return db.scalar(stmt) 
    
