import sqlite3
from models import Book, Review


def initialize_database():
    conn = sqlite3.connect('book_reviews.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS books
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    author TEXT,
                    publication_year INTEGER)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS reviews
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    book_id INTEGER,
                    text TEXT,
                    rating INTEGER)''')
    conn.commit()
    conn.close()


def add_book_to_db(book: Book):
    conn = sqlite3.connect('book_reviews.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO books (title, author, publication_year) VALUES (?, ?, ?)',
                   (book.title, book.author, book.publication_year))
    conn.commit()
    conn.close()


def add_review_to_db(review: Review):
    conn = sqlite3.connect('book_reviews.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO reviews (book_id, text, rating) VALUES (?, ?, ?)',
                   (review.book_id, review.text, review.rating))
    conn.commit()
    conn.close()


def get_books_from_db(author: str = None, publication_year: int = None):
    conn = sqlite3.connect('book_reviews.db')
    cursor = conn.cursor()

    query = 'SELECT * FROM books'
    if author:
        query += f' WHERE author="{author}"'
    if publication_year:
        query += f' WHERE publication_year={publication_year}'
    cursor.execute(query)
    books = cursor.fetchall()

    conn.close()
    return books


def get_reviews_from_db(book_id: int):
    conn = sqlite3.connect('book_reviews.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM reviews WHERE book_id=?', (book_id,))
    reviews = cursor.fetchall()

    conn.close()
    return reviews
