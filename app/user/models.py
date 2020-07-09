from .. import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String)
    email = db.Column(db.String)

    def __init__(self, name, password, email, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.password = password
        self.email = email

    def __repr__(self):
        return f'{self.username}'
