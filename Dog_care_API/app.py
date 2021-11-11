import flask
from flask import Flask, jsonify, request
from flask_cors import CORS
from models import Order


app = Flask(__name__)
CORS(app)

memory_users = []
memory_orders = []
memory_dogs = []
order_id = 0


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/api/v1/orders', methods=["GET", "POST"])
def Orders():
    is_create = flask.request.method == 'POST'
    is_get_all = flask.request.method == 'GET'

    if is_create:
        body = flask.request.json
        order_id_gen = generate_order_id()
        new_order = Order(
            order_id_gen,
            body["name"],
            body["surname"],
            body["phoneNumber"],
            body["location"],
            body["postalCode"],
            body["email"],
            body["pedidos"]
        )
        memory_orders.append(new_order.to_json())
        return {"Orden": new_order.to_json(), "mensaje": "Orden creada exitosamente", "status": "ok"}

    if is_get_all:
        return jsonify(memory_orders)


def generate_order_id():
    order_id.__add__(1)
    return str((len(memory_orders) + 1)).rjust(10, "0")


@app.route('/api/v1/registros', methods=["GET", "POST"])
def registros():
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


@app.route('/api/v1/perros', methods=["GET", "POST"])
def Dogs():
    is_created = flask.request.method == 'POST'
    is_get = flask.request.method == 'GET'

    if is_created:
        body = flask.request.json
        new_dog = {
           "name": body["name"],
           "raza": body["raza"],
           "edad": body["edad"],
           "lugar": body["lugar"],
       }
        memory_dogs.append(new_dog)
        return jsonify({"infoPerro": new_dog, "mensaje": "Perro agregado exitosamente", "status": "ok"})

    if is_get:
        return jsonify(memory_dogs)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)