import time
from fastapi import FastAPI, Request

app = FastAPI()


# request시, 응답시 2번 실행되어 process time을 측정
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/")
async def hello():
    return {"message": "Hello World"}