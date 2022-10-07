import os
from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY= os.environ.get('SECRET_KEY'),
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE=os.environ.get('FLASK_DATABASE'),
    )

    from . import db

    db.init_app(app)

    #### importar el blue print

    from . import register

    app.register_blueprint(register.bp)

    return app
