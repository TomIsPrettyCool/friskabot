from flask_sqlalchemy import SQLAlchemy
from google.appengine.ext import ndb

class Orders(ndb.Model):
    user_id = ndb.StringProperty()
    user_name = ndb.StringProperty()
    order = ndb.StringProperty()

    def __init__(self, id, name, order):
        self.user_id = id
        self.user_name = name
        self.order = order



