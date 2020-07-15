from werkzeug import generate_password_hash, check_password_hash

from app import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(127), unique=True, index=True, nullable=False)
    first_name = db.Column(db.String(127), nullable=False)
    last_name = db.Column(db.String(127), nullable=False)
    email = db.Column(db.String(127), nullable=False)
    password = db.Column(db.String(127), nullable=False)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)

    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'))

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
