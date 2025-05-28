from lib.db.connection import session
from lib.models.book import Book

def add_book(title, author):
    book = Book(title=title, author=author)
    session.add(book)
    session.commit()
    print(f"Book '{title}' by {author} added.")

def list_books():
    books = session.query(Book).all()
    for book in books:
        print(f"{book.id}: '{book.title}' by {book.author}")
