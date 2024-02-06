from flask import make_response


def get_all_users():

    data = [
        {"id": 1, "name": "John Doe"},
        {"id": 2, "name": "Jane Doe"}
    ]

    response = make_response(data, 200)

    return response


def get_all_animais():

    data = [
        {"id": 1, "name": "cachorro"},
        {"id": 2, "name": "vaca"}
    ]

    response = make_response(data, 200)

    return response