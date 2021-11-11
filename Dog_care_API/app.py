import flask
from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

memory_users = []
memory_orders = []
memory_dogs = []

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

@app.route('/api/v1/orden', methods=["GET", "POST"])
def crearOrden():
    is_created = flask.request.method == 'POST'
    is_get = flask.request.method == 'GET'

    if is_created:
        body = flask.request.json
        nueva_orden = {
           "name": body["name"],
           "surname": body["surname"],
           "phoneNumber": body["phoneNumber"],
           "location": body["location"],
           "postalCode": body["postalCode"],
           "email": body["email"],
           "pedidos": body["pedidos"],
       }
        memory_orders.append(nueva_orden)
        return jsonify({"Orden": nueva_orden, "mensaje": "Orden creada exitosamente", "status": "ok"})

    if is_get:
        return jsonify(memory_orders)

@app.route('/api/v1/perro', methods=["GET", "POST"])
def crearPerro():
    is_created = flask.request.method == 'POST'
    is_get = flask.request.method == 'GET'

    if is_created:
        body = flask.request.json
        nuevo_perro = {
           "name": body["name"],
           "raza": body["raza"],
           "edad": body["edad"],
           "lugar": body["lugar"],
       }
        memory_dogs.append(nuevo_perro)
        return jsonify({"infoPerro": nuevo_perro, "mensaje": "Perro agregado exitosamente", "status": "ok"})

    if is_get:
        return jsonify(memory_orders)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
