from app.database.database import get_db_connection

def create_user(name: str, email: str, phone_number: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email, phone_number) VALUES (?, ?, ?)",
                   (name, email, phone_number))
    conn.commit()
    conn.close()

def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

def update_user(id: int, name: str, email: str, phone_number: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = ?, email = ?, phone_number = ? WHERE id = ?",
                   (name, email, phone_number, id))
    conn.commit()
    conn.close()

def delete_user(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()
    conn.close()
