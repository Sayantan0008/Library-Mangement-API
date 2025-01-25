from app.database.borrow_models import create_borrow_record, return_book
from app.database.models import get_books

def borrow_book(book_id: int, user_id: int):
    books = get_books()
    book_available = any(book['id'] == book_id for book in books if not book['is_borrowed'])
    
    if not book_available:
        return {"message": "Book is not available for borrowing."}
    
    # Logic to create a borrow record
    borrow_record = create_borrow_record(book_id, user_id, "2023-10-01", None, False)
    return {"message": "Book borrowed successfully.", "borrow_record": borrow_record}

def return_borrowed_book(record_id: int):
    return_book(record_id)
    return {"message": "Book returned successfully."}
