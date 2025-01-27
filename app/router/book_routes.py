from fastapi import APIRouter

router = APIRouter()

@router.post("/books")
async def add_book(book: dict):
    return {"message": "Book added", "book": book}

@router.get("/books")
async def get_books():
    return {"message": "List of books"}

@router.put("/books/{id}")
async def update_book(id: int, book: dict):
    return {"message": "Book updated", "id": id, "book": book}

@router.delete("/books/{id}")
async def delete_book(id: int):
    return {"message": "Book deleted", "id": id}
