from app import db


class Address(db):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(63))
    city = db.Column(db.String(63))
    street = db.Column(db.String(63))
    description = db.Column(db.Text)

    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'), nullable=False)

    def __str__(self):
        return f"{', '.join(item for item in (self.country, self.city, self.street))}"
