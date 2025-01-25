from .borrowing_service import borrow_book, return_borrowed_book

def test_borrow_book():
    print("Testing borrow_book function...")
    result = borrow_book(1, 1)  # Assuming book_id=1 and user_id=1
    print(result)

def test_return_borrowed_book():
    print("Testing return_borrowed_book function...")
    result = return_borrowed_book(1)  # Assuming record_id=1
    print(result)

if __name__ == "__main__":
    test_borrow_book()
    test_return_borrowed_book()
