from models import Orders, Soups
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

        with open('config.json', 'r') as config:
            token = json.load(config)['token']
        print(str(token))
        if self.token in token:
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
        order = Orders(id=self.user_id, user_name=self.user_name, order=order_string)
        response = order.put()
        return 'Order Submitted/Updated'

    def soups(self):
        soups = Soups.get_by_id(id='soup')
        string = ""
        for soup in soups.soup_array:
            string += soup + "\n"   #Dodgy formatting
        return "The soups today are: \n```" + string + "```" #Chop end off string to account for previous mistakes

    def view(self):
        query = Orders.query()
        return_string = "```"
        for x in query:
            return_string += "{} ordered {} \n".format(x.user_name, x.order)
        return return_string + "```"

    def me(self):
        return 'You are now designated to get orders'

    def help(self):
        return 'Self explanatory'
