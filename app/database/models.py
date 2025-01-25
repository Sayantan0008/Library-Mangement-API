from app.database.database import get_db_connection

def create_book(title: str, author: str, genre: str, publication_year: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, genre, publication_year) VALUES (?, ?, ?, ?)",
                   (title, author, genre, publication_year))
    conn.commit()
    conn.close()

def get_books():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return books

def update_book(id: int, title: str, author: str, genre: str, publication_year: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET title = ?, author = ?, genre = ?, publication_year = ? WHERE id = ?",
                   (title, author, genre, publication_year, id))
    conn.commit()
    conn.close()

def delete_book(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (id,))
    conn.commit()
    conn.close()
