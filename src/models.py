from flask_sqlalchemy import SQLAlchemy
from google.appengine.ext import ndb


class Orders(ndb.Model):
    user_name = ndb.StringProperty()
    order = ndb.StringProperty()


class Soups(ndb.Model):
    soup_array = ndb.StringProperty(repeated=True)