from pydantic import BaseModel


class Book(BaseModel):
    title: str
    author: str
    publication_year: int


class Review(BaseModel):
    book_id: int
    text: str
    rating: int
