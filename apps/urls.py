
from apps.controllers import ApiViewAnimal, ApiViewUsers, Login


def add_routes(app):
    app.add_url_rule('/animais', view_func=ApiViewAnimal.as_view('animais'))
    app.add_url_rule('/users', view_func=ApiViewUsers.as_view('users'))
    app.add_url_rule('/login', view_func=Login.as_view('login'))