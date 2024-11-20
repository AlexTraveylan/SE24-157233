from typing import Annotated

from fastapi import Depends, FastAPI

from src.database import FakeDB, get_db

app = FastAPI()


@app.get("/")
def read_root(name: str):
    return {"message": f"Hello, {name}!"}


@app.get("/books")
def get_books(database: Annotated[FakeDB, Depends(get_db)]):
    return database.get_all_books()


@app.get("/books/{book_id}")
def get_book_by_id(book_id: int, database: Annotated[FakeDB, Depends(get_db)]):
    return database.get_book_by_id(book_id)
