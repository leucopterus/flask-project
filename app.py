from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/ede/Desktop/innowise/projects/flask-project/data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '@#_VIHn)@P#OLDih@#PBIKW:A928yrfhy'

db = SQLAlchemy(app)


if __name__ == '__main__':
    app.run()
