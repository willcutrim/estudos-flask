from flask import Flask, request, jsonify
from flask.views import MethodView
from apps.utils import get_all_users, get_all_animais

app = Flask(__name__)


class ApiViewUsers(MethodView):
    def get(self):
        return get_all_users()

class ApiViewAnimal(MethodView):
    def get(self):
        return get_all_animais()


if __name__ == '__main__':
    app.run(debug=True)
