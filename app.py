from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from db import db
from routers import initialize_routers
from security import authenticate, identity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'asdf-9213uf-cHJN(_#@yfhco#@*p:a='
api = Api(app)
initialize_routers(api)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
