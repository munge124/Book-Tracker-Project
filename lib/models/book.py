from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.connection import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)

    reading_statuses = relationship('ReadingStatus', back_populates='book', cascade='all, delete-orphan')
