import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add_book():
    response = client.post("/books", json={"title": "Test Book", "author": "Author", "genre": "Fiction", "publication_year": 2021})
    assert response.status_code == 200
    assert response.json() == {"message": "Book added", "book": {"title": "Test Book", "author": "Author", "genre": "Fiction", "publication_year": 2021}}

def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert "books" in response.json()  # Check that the response contains the 'books' key
    assert isinstance(response.json()["books"], list)  # Ensure that the value is a list

def test_add_user():
    response = client.post("/users", json={"name": "Test User", "email": "test@example.com", "phone_number": "1234567890"})
    assert response.status_code == 200
    assert response.json() == {"message": "User added", "user": {"name": "Test User", "email": "test@example.com", "phone_number": "1234567890"}}

def test_delete_book():
    # First, add a book to ensure there is one to delete
    client.post("/books", json={"title": "Test Book", "author": "Author", "genre": "Fiction", "publication_year": 2021})
    
    # Now delete the book
    response = client.delete("/books/1")  # Assuming the ID of the book is 1
    assert response.status_code == 200
    assert response.json() == {"message": "Book deleted", "id": 1}

def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert "List of users" in response.json().values()
