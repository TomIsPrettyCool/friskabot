from flask import Flask, request


app = Flask(__name__)

commands = ['/order', '/availiable','/view', '/menu']


@app.route('/api/')
def api():
    args = request.args
    command = args.get('command')

    init_command = command.split(' ')[0]

    if init_command in commands:
        return 'yay'
    else:
        return 'arse'

def order():
    pass

def availiable():
    pass
