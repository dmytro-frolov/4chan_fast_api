import uvicorn
import bs4
import requests

from fastapi import FastAPI
from lxml import html

from views import Board

app = FastAPI()


@app.get("/{board_name}/{thread}")
async def thread(board_name: str, thread: str):
    return {}

@app.get("/{board_name}")
async def board(board_name: str):
    r = requests.get(f'https://4chan.org/{board_name}')
    tree = html.fromstring(r.content)

    board = Board(tree)
    board.parse()

    return board.to_json()

@app.get("/")
async def root():
    return {}

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000)