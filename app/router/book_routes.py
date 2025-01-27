from fastapi import APIRouter
from app.database.models import create_book, delete_book, get_books  # Importing the necessary functions

router = APIRouter()

@router.post("/books")
async def add_book(book: dict):
    required_fields = ["title", "author", "genre", "publication_year"]
    for field in required_fields:
        if field not in book:
            return {"error": f"Missing field: {field}"}, 400

    title = book["title"]
    author = book["author"]
    genre = book["genre"]
    publication_year = book["publication_year"]
    create_book(title, author, genre, publication_year)
    return {"message": "Book added", "book": book}

@router.get("/books")
async def fetch_books():
    books = get_books()  # Call the database function to retrieve books
    return {"books": books}

@router.put("/books/{id}")
async def update_book(id: int, book: dict):
    required_fields = ["title", "author", "genre", "publication_year"]
    for field in required_fields:
        if field not in book:
            return {"error": f"Missing field: {field}"}, 400

    title = book["title"]
    author = book["author"]
    genre = book["genre"]
    publication_year = book["publication_year"]
    update_book(id, title, author, genre, publication_year)  # Call the database function to update the book
    return {"message": "Book updated", "id": id, "book": book}

@router.delete("/books/{id}")
async def delete_book_route(id: int):
    delete_book(id)  # Call the database function to delete the book
    return {"message": "Book deleted", "id": id}
