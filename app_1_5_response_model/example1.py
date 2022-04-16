from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl


app = FastAPI()


class User(BaseModel):
    name: str
    avatar_url: HttpUrl = "https://icotar.com/avatar/fastcampus.png?s=200"


class CreateUser(User):
    password: str


@app.post("/users", response_model=User)
def create_user(user: CreateUser):
    return user
