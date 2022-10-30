from fastapi import FastAPI
from pydantic import BaseModel

from database.memo import Memo

app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}


class MemoOut(BaseModel):
    title: str
    body: str


@app.get('/memos')  # 모두가 double quote 를 쓰지만 나는 single quote 쓰고 싶은데?
async def get_all_memos() -> list[MemoOut]:
    memos = await Memo.all()
    return [MemoOut(title=memo.title, body=memo.body) for memo in memos]
