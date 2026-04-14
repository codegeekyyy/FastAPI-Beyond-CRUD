import json
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


# Load books data from the JSON file
with open("books.json", "r") as f:
    books = json.load(f)


@app.get('/books', response_model=List[Book], status_code=200)
async def get_all_books():
    return books


# response_model ensures your API:
# - Returns correct data shape
# - Hides unwanted fields
# - Generates clean documentation
# - Improves reliability and safety
@app.post('/books', response_model=dict)
async def create_a_book(book_data: Book):
    books.append(book_data.model_dump())
    return {"message": "Book created successfully"}


@app.get('/books/{book_id}')
async def get_a_book(book_id: int) -> dict:
    pass


@app.put('/books/{book_id}')
async def update_a_book(book_id: int) -> dict:
    pass


@app.delete('/books/{book_id}')
async def delete_a_book(book_id: int) -> dict:
    pass