from fastapi import FastAPI, HTTPException, BackgroundTasks
from models import Book, Review
from database import add_book_to_db, get_books_from_db, get_reviews_from_db
from bg_task import add_review
from database import initialize_database

app = FastAPI()

initialize_database()


@app.get("/")
async def healthy():
    return {
        "message": "Your App is running successfully.",
        "status": True
    }


@app.post("/books/")
async def create_book(book: Book):
    add_book_to_db(book)
    return {"message": "Book added successfully"}


@app.post("/reviews/")
async def create_review(review: Review, background_tasks: BackgroundTasks):
    return add_review(review, background_tasks)


@app.get("/books/")
async def retrieve_books(author: str = None, publication_year: int = None):
    return get_books_from_db(author, publication_year)


@app.get("/reviews/{book_id}")
async def retrieve_reviews(book_id: int):
    return get_reviews_from_db(book_id)
