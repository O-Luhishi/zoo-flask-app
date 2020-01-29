# app/models.py

from app import db


class Animal(db.Model):
    """
    Create a Department table
    """

    __tablename__ = 'Animal'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))

    def __repr__(self):
        return '<Animal: {}>'.format(self.name)