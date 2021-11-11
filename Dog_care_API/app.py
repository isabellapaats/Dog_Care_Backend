import flask
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

memory_users = []


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/api/v1/registro', methods=["GET", "POST"])
def registrarse():
    is_registered = flask.request.method == 'POST'
    is_get = flask.request.method == 'GET'

    if is_registered:
        body = flask.request.json
        nuevo_usuario = Usuarios(
            body["user"],
            body["surname"],
            body["email"],
            body["password"],
        )
        memory_users.append(nuevo_usuario.to_json())

    return flask.jsonify(nuevo_usuario)

    if is_get:
        return flask.jsonify(memory_users)


class Usuarios:
    def _init_(self, user_name, user_surname, user_email, user_password):
        self.user_name = user_name
        self.user_surname = user_surname
        self.user_email = user_email
        self.user_password = user_password

    def to_json(self):
        return self._dict_


if __name__ == '_main_':
    app.run()