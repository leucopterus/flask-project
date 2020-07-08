from sqlalchemy import Column, Integer, String

from api.resources.core.schema import Base


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String(127))
    author = Column(String(63))
    pages = Column(Integer)

    def __repr__(self):
        return f'<Book(title={self.title}, author={self.author}, ' \
               f'pages={self.pages})>'
