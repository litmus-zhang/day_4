from flask import Blueprint

user = Blueprint('user', __name__)

@user.route('/')

def index():
    return '<h1>User index, extending the Day 3 task <h1>'