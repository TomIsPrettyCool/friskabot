from flask import Flask, request
from commands import ProcessCommand
app = Flask(__name__)


@app.route('/api/')
def api():
    args = request.args

    command = ProcessCommand(args)
    if command.verify_token():
        return command.process_command()
    else:
        return 'Failed request. Invalid token'




