from fastapi import FastAPI

app = FastAPI()


# /user/{user_id}가 위에있으면 /user/{user_id}에 의해 처리되므로 /users/me가 위에 있어야함.
@app.get("/users/me")
def get_current_user():
    return {"user_id": 123}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}