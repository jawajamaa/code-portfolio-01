from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Code Model view only
class Code(db.Model, SerializerMixin):
    __tablename__ = 'documents'

    id = db.Column(db.Integer, primary_key = True)
    item = db.Column(db.String)
    path = db.Column(db.String)


class Image(db.Model, SerializerMixin):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    location = db.Column(db.String)
    year = db.Column(db.Integer)
    gallery = db.Column(db.String)
    horizontal = db.Column(db.Boolean)
    path = db.Column(db.String)

class PopQuiz(db.Model, SerializerMixin):
    __tablename__ = "popquizquestions"

    id = db.Column(db.Integer, primary_key = True)
    question = db.Column(db.String)
    answer = db.Column(db.String)

# Photography Model views - not needed? 
# class Airport(db.Model, SerializerMixin):
#     pass

# class FromTheHip(db.Model, SerializerMixin):
#     pass

# class Place(db.Model, SerializerMixin):
#     pass

# class Space(db.Model, SerializerMixin):
#     pass
