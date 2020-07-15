from app import db
from api.models.user import User
from api.models.publisher import Publisher


authors = db.Table(
    'authors',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True)
)


class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(127), unique=True, index=True)
    authors = db.relationship(User, secondary=authors, lazy='subquery',
                              backref=db.backref('books', lazy=True))
    publisher = db.relationship(Publisher, lazy='select',
                                backref=db.backref('book', lazy='joined'))

    def __str__(self):
        return f'{self.title}'
