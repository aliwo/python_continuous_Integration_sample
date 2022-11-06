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


@app.get("/memos")
async def get_all_memos() -> list[dict[str, str]]:
    memos = await Memo.all()
    return [MemoOut(title=memo.title, body=memo.body) for memo in memos]
