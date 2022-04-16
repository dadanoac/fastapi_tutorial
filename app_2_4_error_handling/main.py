from typing import Any, Optional, Dict

from fastapi import FastAPI, HTTPException


# fastAPI 기본 error class 이용
class SomeFastAPIError(HTTPException):
    def __init__(
        self,
        status_code: int,
        detail: Any = None,
        headers: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(
            status_code=status_code, detail=detail, headers=headers
        )


app = FastAPI()


@app.get("/error")
async def get_error():
    raise SomeFastAPIError(500, "Hello")

# 사용자 정의 err
# from fastapi import FastAPI, Request
# from fastapi.responses import JSONResponse

# app = FastAPI()


# class SomeError(Exception):
#     def __init__(self, name: str, code: int):
#         self.name = name
#         self.code = code

#     def __str__(self):
#         return f"<{self.name}> is occured. code: <{self.code}>"


# app = FastAPI()


# # 추가
# @app.exception_handler(SomeError)
# async def some_error_handler(request: Request, exc: SomeError):
#     return JSONResponse(
#         content={"message": f"error is {exc.name}"}, status_code=exc.code
#     )


# @app.get("/error")
# async def get_error():
#     raise SomeError("Hello", 500)