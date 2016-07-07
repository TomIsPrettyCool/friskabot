from flask import Flask, request
from commands import ProcessCommand
from webscraper import GetSoup
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///friska.db'
db = SQLAlchemy(app)

GetSoup().extract_backround()


@app.route('/api/')
def api():
    args = request.args

    command = ProcessCommand(args)
    if command.verify_token():
        return command.process_command()
    else:
        return 'Failed request. Invalid token'




