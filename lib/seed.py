from lib.connection import session
from lib.models.user import User
from lib.models.book import Book
from lib.models.reading_status import ReadingStatus

def seed_data():
    user1 = User(name="Alice")
    book1 = Book(title="1984", author="George Orwell")
    book2 = Book(title="The Hobbit", author="J.R.R. Tolkien")

    status1 = ReadingStatus(status="Reading", user=user1, book=book1)
    status2 = ReadingStatus(status="Completed", user=user1, book=book2)

    session.add_all([user1, book1, book2, status1, status2])
    session.commit()
