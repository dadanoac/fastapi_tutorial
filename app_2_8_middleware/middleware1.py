# 백엔드 ↔ 프론트 서버가 분리되었을때 난감한 부분이 있습니다. 
# 바로 XSS를 막기 위한 동일 출처 정책 때문에 발생하는 문제
# 정확히는 CORS(https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost",
    "https://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["OPTIONS", "GET"],
    allow_headers=["*"],
)


@app.get("/")
async def hello():
    return {"message": "Hello World"}