from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Float,
    String,
    Date,
)
from sqlalchemy.orm import relationship

from resources.core.schema import Base


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String(127))
    author_id = Column(Integer, ForeignKey('users.id'))
    price = Column(Float)
    written = Column(Date)

    author = relationship('User', back_populates='books')

    def __str__(self):
        return f'{self.title} written by {self.author}'
