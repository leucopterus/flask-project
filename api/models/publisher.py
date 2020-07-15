from app import db
from api.models.address import Address
from api.models.user import User


class Publisher(db.Model):
    __tablename__ = 'publisher'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(127), unique=True, index=True)
    address = db.relationship(Address, uselist=False, lazy='select',
                              backref=db.backref('publisher', lazy='joined'))
    owner = db.relationship(User, lazy='select',
                            backref=db.backref('publisher', lazy='joined'))

    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    def __str__(self):
        return f'Publisher {self.name}'
