# README

## Library Management System API

### Overview

The Library Management System API is a RESTful service for managing books, users, and borrowing records in a library. It supports CRUD operations, book borrowing/returning logic, and database integration using SQLite. The API adheres to clean coding practices and is tested using Postman and unit tests.

---

### Features

1. **Book Management:**

   - Add new books to the library.
   - Retrieve a list of all books with optional filters for author and genre.
   - Update book details.
   - Delete books from the library.

2. **User Management:**

   - Add new users.
   - Retrieve a list of all users.
   - Update user details.
   - Delete users from the system.

3. **Borrow & Return Management:**

   - Borrow books, creating a borrowing record.
   - Mark books as returned.
   - Prevent borrowing of already borrowed books.

---

### Requirements

To run the project, ensure you have the following installed:

- Python 3.8+
- SQLite

---

### Installation

1. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python app/main.py
   ```

---

### Folder Structure

```
library-management-system/
├── app/                # Main application code
│   ├── routes/         # API route handlers
│   ├── database/       # Database connection and models
│   └── services/       # Core functionalities (e.g., borrowing logic)
├── tests/              # Unit tests for key functionalities
├── README.md           # Setup instructions and API documentation
└── requirements.txt    # Dependencies
```

---

### API Endpoints

#### Books

- `POST /books` - Add a new book.
- `GET /books` - Retrieve all books (supports filters by author and genre).
- `PUT /books/{id}` - Update a specific book.
- `DELETE /books/{id}` - Delete a specific book.

#### Users

- `POST /users` - Add a new user.
- `GET /users` - Retrieve all users.
- `PUT /users/{id}` - Update a specific user.
- `DELETE /users/{id}` - Delete a specific user.

#### Borrow Records

- `POST /borrow` - Borrow a book (check availability first).
- `PUT /return/{id}` - Mark a book as returned.

---

### Testing

1. Use Postman or cURL to test endpoints. Example cURL command to add a book:

   ```bash
   curl -X POST http://127.0.0.1:5000/books -H "Content-Type: application/json" -d '{"title": "Book Title", "author": "Author Name", "genre": "Genre", "publication_year": 2023}'
   ```

2. Run unit tests:

   ```bash
   python -m unittest discover tests/
   ```

---

### License

This project is licensed under the MIT License.

---



