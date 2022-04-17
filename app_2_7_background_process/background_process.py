import time

from fastapi import BackgroundTasks, FastAPI, status

app = FastAPI()


def write_log(message: str):
    time.sleep(2.0)

    with open("log.txt", mode="a") as log:
        log.write(message)


@app.post("/send-notification/{email}", status_code=status.HTTP_202_ACCEPTED)
async def send_notification(email: str, background_tasks: BackgroundTasks):
    message = f"message to {email}\n"
    # write_log 함수를 message라는 인자를 이용하여 background에서 실행
    # failover 처리가 힘듬.
    # 작업이 클 경우 queue를 만들어 처리
    background_tasks.add_task(write_log, message)

    return {"message": "Message sent"}
