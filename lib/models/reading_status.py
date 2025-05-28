from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from lib.db.connection import Base

class ReadingStatus(Base):
    __tablename__ = 'reading_statuses'

    id = Column(Integer, primary_key=True)
    status = Column(String, nullable=False)  
    user_id = Column(Integer, ForeignKey('users.id'))
    book_id = Column(Integer, ForeignKey('books.id'))

    user = relationship('User', back_populates='reading_statuses')
    book = relationship('Book', back_populates='reading_statuses')
