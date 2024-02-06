from flask import Flask
from apps.urls import add_routes

app = Flask(__name__)


add_routes(app)


if __name__ == '__main__':
    app.run()