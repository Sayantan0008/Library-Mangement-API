import sqlite3

def init_db():
    conn = sqlite3.connect('library.db')  # Connect to the correct database file
    cursor = conn.cursor()

    # Create books table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        genre TEXT NOT NULL,
        publication_year INTEGER NOT NULL
    )
    ''')

    # Create borrow_records table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS borrow_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        borrow_date TEXT NOT NULL,
        return_date TEXT,
        is_returned BOOLEAN NOT NULL,
        FOREIGN KEY (book_id) REFERENCES books (id)
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
