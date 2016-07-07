from models import Orders, db
commands = ["order", "soups", "view", "me", "help"]
import json


class ProcessCommand:
    def __init__(self, data):
        """
        Pull needed data from request args
        """
        self.data = data.get('text')
        self.url_to_return = data.get('response_url')
        self.user_name = data.get('user_name')
        self.user_id = data.get('user_id')
        self.token = data.get('token')

        self.data_parsed = self.data.split(' ')

    def verify_token(self):
        """
        Verify request is legitimate
        """
        if self.token == 'hhOF3oMoHROCcXP1aWEIgig7':
            return 'Token Verified'
        else:
            return False

    def process_command(self):
        if self.data_parsed[0] in commands:
            function = getattr(self, self.data_parsed[0])
            return function()
        else:
            return 'not a valid command, try `/friska help`'

    def order(self):
        order_string = ""
        for order_text in self.data_parsed[1:]:
            order_string += order_text + " "
        payload = Orders(self.user_id, self.user_name, order_string)
        db.session.add(payload)
        db.session.commit()
        return 'Order Submitted, now beg someone to go get it :' + order_string

    def soups(self):
        with open('soups.json') as cache:
            soups = json.load(cache)
        string = ""
        for soup in soups["soups"]:
            string += soup + " | "
        return string

    def view(self):
        query = Orders.query.order_by(Orders.id)
        return_string = "```"
        for x in query:
            return_string += "{} ordered {} \n".format(x.user_name, x.order)
        return return_string + "```"

    def me(self):
        return 'You are now designated to get orders'

    def help(self):
        return 'Self explanatory'
