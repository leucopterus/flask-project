from app import db
from api.models.address import AddressModel
from api.models.user import UserModel


class PublisherModel(db.Model):
    __tablename__ = 'publisher'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(127), unique=True, index=True)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))
    address = db.relationship(AddressModel, uselist=False, lazy='select',
                              backref=db.backref('publisher', lazy='joined'))
    owner_id = db.relationship(db.Integer, db.ForeignKey('user.id'))
    owner = db.relationship(UserModel, lazy='select',
                            backref=db.backref('publisher', lazy='joined'))

    def __str__(self):
        return f'Publisher {self.name}'
