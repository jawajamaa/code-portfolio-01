from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

class Space(db.Model, SerializerMixin):
    pass

class Place(db.Model, SerializerMixin):
    pass

class Airport(db.Model, SerializerMixin):
    pass

class FromTheHip(db.Model, SerializerMixin):
    pass
