FROM flask_sqlalchemy IMPORT SQLAlchemy
db= SQLAlchemy()

def connect_db(app):
    """ Connects to database """

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    