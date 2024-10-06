from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/world')
def index():
    return "Hello World"