from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Dragon(db.Model):
    __tablename__ = "dragons"
    dragon_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    dragon_name = db.Column(db.String(64))
    place_id = db.Column(db.Integer, db.ForeignKey('places.place_id'))


class Place(db.Model):
    __tablename__ = "places"
    place_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    place_name = db.Column(db.String(64))
    dragons = db.relationship("Dragon", backref=db.backref("places", order_by=place_id))



def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///dragons'
    db.app = app
    db.init_app(app)
    db.create_all()
    db.session.commit()
