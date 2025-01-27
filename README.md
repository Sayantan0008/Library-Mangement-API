
# Library Management System API

## Overview
The Library Management System API is a RESTful service for managing books, users, and borrowing records in a library. It supports CRUD operations for books and users.
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
## API Endpoints

### Books
- **POST /books**: Add a new book.
- **GET /books**: Retrieve all books (supports filters by author and genre).
- **PUT /books/{id}**: Update a specific book.
- **DELETE /books/{id}**: Delete a specific book.

### Users
- **POST /users**: Add a new user.
- **GET /users**: Retrieve all users.
- **PUT /users/{id}**: Update a specific user.
- **DELETE /users/{id}**: Delete a specific user.

### Borrow Records
- **POST /borrow**: Borrow a book (check availability first).
- **PUT /return/{id}**: Mark a book as returned.

## Usage Instructions
You can use Postman or cURL to test the endpoints. Here’s an example cURL command to add a book:

```bash
curl -X POST http://127.0.0.1:8000/books -H "Content-Type: application/json" -d '{"title": "Book Title", "author": "Author Name", "genre": "Genre", "publication_year": 2023}'
```

## Testing
To run the tests for the API, use the following command:

```bash
pytest tests/test_api.py
```
---
### License

This project is licensed under the MIT License.

---
