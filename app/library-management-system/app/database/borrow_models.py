from app.database.database import get_db_connection

def create_borrow_record(book_id: int, user_id: int, borrow_date: str, return_date: str, is_returned: bool):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO borrow_records (book_id, user_id, borrow_date, return_date, is_returned) VALUES (?, ?, ?, ?, ?)",
                   (book_id, user_id, borrow_date, return_date, is_returned))
    conn.commit()
    conn.close()

def get_borrow_records():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM borrow_records")
    records = cursor.fetchall()
    conn.close()
    return records

def return_book(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE borrow_records SET is_returned = ? WHERE id = ?", (True, id))
    conn.commit()
    conn.close()
