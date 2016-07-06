commands = ["order", "menu", "view", "me", "help"]

class ProcessCommand:
    def __init__(self, data):
        self.data = data.get('text')
        self.url_to_return = data.get('response_url')
        self.user_name = data.get('user_name')
        self.token = data.get('token')

        self.data_parsed = self.data.split(' ')

    def verify_token(self):
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

    def menu(self):
        pass
    def view(self):
        pass
    def me(self):
        pass
    def help(self):
        pass