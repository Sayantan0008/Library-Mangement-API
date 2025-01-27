from fastapi import APIRouter
from app.database.models import create_book, delete_book  # Importing the necessary functions

router = APIRouter()

@router.post("/books")
async def add_book(book: dict):
    title = book.get("title")
    author = book.get("author")
    genre = book.get("genre")
    publication_year = book.get("publication_year")
    create_book(title, author, genre, publication_year)
    return {"message": "Book added", "book": book}

@router.get("/books")
async def get_books():
    return {"message": "List of books"}

@router.put("/books/{id}")
async def update_book(id: int, book: dict):
    return {"message": "Book updated", "id": id, "book": book}

@router.delete("/books/{id}")
async def delete_book_route(id: int):
    delete_book(id)  # Call the database function
    return {"message": "Book deleted", "id": id}
