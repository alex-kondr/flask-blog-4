from flask import Flask

from app.db import create_db
from app.routes import position_route


app = Flask(__name__)
app.register_blueprint(position_route)


def main():
    create_db()
    app.run(debug=True)
