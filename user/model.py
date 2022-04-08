from flask import Blueprint

model = Blueprint('user', __name__, url_prefix='/user')

@model.route('/getdata')

def getdata():
    return {'data': 'Hello from Zhang at 30 days of code'}