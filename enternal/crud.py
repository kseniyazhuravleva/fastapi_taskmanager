from sqlalchemy.orm import Session
from . import models, schemas
import bcrypt

def get_users(db: Session):
    return db.query(models.User).all()
    

def get_user(db: Session, id: int):
    return db.query(models.User).get(id)
    
def create_user(db: Session, instance: schemas.CreateUser):
    hashed_password = bcrypt.hashpw(instance.password.encode('utf-8'), bcrypt.gensalt())
    model = models.User(username=instance.username, password=hashed_password)
    db.add(model)
    db.commit()
    return model