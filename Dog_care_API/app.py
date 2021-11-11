import flask
from flask import Flask, jsonify, request
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
        nuevo_registro = {
           "user_name": body["user"],
           "user_surname": body["surname"],
           "user_mail": body["mail"],
           "user_password": body["password"],

       }
        memory_users.append(nuevo_registro)
        return jsonify({"registro": nuevo_registro, "mensaje": "usuario registrado correctamente", "status": "ok"})

    if is_get:
        return "hola"


if __name__ == '_main_':
    app.run()