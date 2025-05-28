from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.db.connection import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    reading_statuses = relationship('ReadingStatus', back_populates='user', cascade='all, delete-orphan')

def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}')>"
