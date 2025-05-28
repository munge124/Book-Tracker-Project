# lib/schema.py

from lib.db.connection import Base, engine
from lib.models.user import User
from lib.models.book import Book
from lib.models.reading_status import ReadingStatus

def create_tables():
    print("Creating database tables...")
    Base.metadata.create_all(engine)
    print("Tables created successfully.")

if __name__ == "__main__":
    create_tables()

