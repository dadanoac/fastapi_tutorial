from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from fastapi_quizbot import models, schemas
from fastapi_quizbot.database import get_db

router = APIRouter()


@router.get("", response_model=List[schemas.User])
async def get_user_list(db: Session = Depends(get_db)):
    return db.query(models.User).all()
