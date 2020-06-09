from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(31))
    last_name = Column(String(31))
    email = Column(String(63))

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
