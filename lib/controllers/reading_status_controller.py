from lib.db.connection import session
from lib.models.reading_status import ReadingStatus
from lib.models.user import User
from lib.models.book import Book

def add_status(user_id, book_id, status):
    user = session.get(User, user_id)
    book = session.get(Book, book_id)
    if user and book:
        reading_status = ReadingStatus(status=status, user=user, book=book)
        session.add(reading_status)
        session.commit()
        print(f"Reading status '{status}' for '{book.title}' added to {user.name}.")
    else:
        print("User or Book not found.")

def view_user_statuses(user_id):
    user = session.get(User, user_id)
    if user:
        for rs in user.reading_statuses:
            print(f"{rs.book.title} - {rs.status}")
    else:
        print("User not found.")
