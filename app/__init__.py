from flask import Flask
from .extensions import db
from .routes.main import main
from .routes.api import api

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(main)
    app.register_blueprint(api)
    return app