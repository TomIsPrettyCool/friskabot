from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from commands import ProcessCommand
from webscraper import GetSoup

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///friska.db'

GetSoup().soup_to_list()

from models import db
db.init_app(app)


@app.route('/api/')
def api():
    args = request.args

    command = ProcessCommand(args)
    if command.verify_token():
        return command.process_command()
    else:
        return 'Failed request. Invalid token'

@app.route('/migrate/')
def migrate():
    db.create_all()
    return 'Created DB'

