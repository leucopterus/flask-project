import json

from flask import (
    Blueprint,
    redirect,
    request,
    session,
    url_for,
)
from app import db
from app.user.models import User

user = Blueprint('user', __name__)


@user.route('/home')
def home():
    body = {'data': 'Hello! this is the main page <h1>HELLO</h1>'}
    return json.dumps(body)


@user.route('/profile')
def profile():
    if session.get('user') is not None and session.get('password') is not None:
        name = session.get('user')
        body = {'data': f'Hello {name}!'}
        return json.dumps(body)
    return redirect(url_for('login'))


@user.route('/admin')
def admin():
    return redirect(url_for('profile', name='superuser'))


@user.route('/register', methods=['POST', 'GET'])
def register():
    if session.get('user') is not None and session.get('password') is not None:
        return redirect(url_for('profile'))
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


@user.route('/login', methods=['POST', 'GET'])
def login():
    if session.get('user') is not None and session.get('password') is not None:
        return redirect(url_for('profile'))
    if request.method == 'POST':
        user_data = json.loads(request.get_data())
        username = user_data.get('username')
        password = user_data.get('password')
        found_user = User.query.filter_by(name=username, password=password).first()
        if found_user:
            session['user'] = username
            session['password'] = password
            return redirect(url_for('profile'))
    body = {'data': 'Please, log in by providing username and password!'}
    return json.dumps(body)


@user.route('/logout')
def logout():
    session['user'] = None
    session['password'] = None
    return redirect(url_for('login'))
