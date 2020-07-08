import json

import sqlalchemy
from flask import Flask, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'askdoqo3wiE)(#dOHqwd#qwnpf870JFU092if'
db = SQLAlchemy(app)

usr_in_db = (
    {'admin': '1234567'},
    {'test': 'tester'},
)


class User(db.Model):
    _id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __init__(self, name, password, email, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.password = password
        self.email = email


@app.route('/')
def home():
    body = {'data': 'Hello! this is the main page <h1>HELLO</h1>'}
    return json.dumps(body)


@app.route('/profile')
def user():
    if session.get('user') is not None and session.get('password') is not None:
        name = session.get('user')
        body = {'data': f'Hello {name}!'}
        return json.dumps(body)
    return redirect(url_for('login'))


@app.route('/admin')
def admin():
    return redirect(url_for('user', name='superuser'))


@app.route('/register', methods=['POST', 'GET'])
def register():
    if session.get('user') is not None and session.get('password') is not None:
        return redirect(url_for('user'))
    if request.method == 'POST':
        user_data = json.loads(request.get_data())
        username = user_data.get('username')
        password = user_data.get('password')
        email = user_data.get('email')
        usr = User(username, password, email)
        db.session.add(usr)
        db.session.commit()
        return redirect(url_for('login'))
    body = {'data': 'Please, register by providing username, password and email address!'}
    return json.dumps(body)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if session.get('user') is not None and session.get('password') is not None:
        return redirect(url_for('user'))
    if request.method == 'POST':
        user_data = json.loads(request.get_data())
        user = user_data.get('username')
        password = user_data.get('password')
        found_user = User.query.filter_by(name=user, password=password).first()
        if found_user:
            session['user'] = user
            session['password'] = password
            return redirect(url_for('user'))
    body = {'data': 'Please, log in by providing username and password!'}
    return json.dumps(body)


@app.route('/logout')
def logout():
    session['user'] = None
    session['password'] = None
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
    db.create_all()
