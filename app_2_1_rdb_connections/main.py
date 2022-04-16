# mysql docker 실행 
# docker run --name fastapi_db \
# -p 3306:3306 \
# -e MYSQL_ROOT_PASSWORD=1234 \
# -e MYSQL_DATABASE=dev -e \
# MYSQL_USER=admin -e \
# MYSQL_PASSWORD=1234 \
# mysql:8.0 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci

from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        print("yield")
        yield db
    finally:
        print("close")
        db.close()


@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existed_user = db.query(models.User).filter_by(
        email=user.email
    ).first()

    if existed_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = models.User(email=user.email, password=user.password)
    db.add(user)
    db.commit()

    return user


@app.get("/users", response_model=List[schemas.User])
def read_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()
