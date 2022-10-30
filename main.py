from pydantic import BaseModel  # Import 순서가 잘못되었습니다.
from fastapi import FastAPI

from database.memo import Memo

app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}


class MemoOut(BaseModel):
    title: str
    body: str


@app.get("/memos")
async def get_all_memos() -> list[MemoOut]:
    memos = await Memo.all()
    return [MemoOut(title=memo.title, body=memo.body) for memo in memos]
