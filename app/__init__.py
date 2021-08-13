from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import jsonify

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    # set configuration variables from config_class for this Flask app
    app.config.from_object(Config)

    # Tell our Flask application to use SQLAlchemy and Migrate and LoginManager
    db.init_app(app)
    migrate.init_app(app, db)

    from app.blueprints.api import bp as api
    app.register_blueprint(api)
    return app





