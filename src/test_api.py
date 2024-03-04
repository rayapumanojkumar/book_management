import pytest
from fastapi.testclient import TestClient
from api import app
from database import initialize_database

client = TestClient(app)


@pytest.fixture(scope="function")
def test_app():
    initialize_database()
    yield app


def test_create_book(test_app):
    # Test valid book creation
    response = client.post("/books/", json={"title": "Book Title", "author": "Author Name", "publication_year": 2022})
    assert response.status_code == 200
    assert response.json() == {"message": "Book added successfully"}

    # Test invalid book creation (missing fields)
    response = client.post("/books/", json={"title": "Book Title", "author": "Author Name"})
    assert response.status_code == 422


def test_create_review(test_app):
    # Test valid review creation
    response = client.post("/reviews/", json={"book_id": 1, "text": "Good book", "rating": 5})
    assert response.status_code == 200

    # Test invalid review creation (missing fields)
    response = client.post("/reviews/", json={"book_id": 1, "text": "Good book"})
    assert response.status_code == 422


def test_retrieve_books(test_app):
    # Test retrieving all books
    response = client.get("/books/")
    assert response.status_code == 200

    # Test retrieving books by author
    response = client.get("/books/?author=Author Name")
    assert response.status_code == 200

    # Test retrieving books by publication year
    response = client.get("/books/?publication_year=2022")
    assert response.status_code == 200


def test_retrieve_reviews(test_app):
    # Test retrieving reviews for a book
    response = client.get("/reviews/1")
    assert response.status_code == 200
