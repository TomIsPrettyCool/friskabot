from friskabot import db


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50))
    user_name = db.Column(db.String(100))
    order = db.Column(db.String(1000))

    def __init__(self, id, name, order):
        self.user_id = id
        self.user_name = name
        self.order = order


