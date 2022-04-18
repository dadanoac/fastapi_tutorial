from sqlalchemy import Column, Integer, String

from fastapi_quizbot.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(String(20), primary_key=True)
    username = Column(String(100), nullable=False)
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))
