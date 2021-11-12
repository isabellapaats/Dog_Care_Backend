import flask
from flask import Flask, jsonify, request
from flask_cors import CORS
from models import Order, User, Dog

app = Flask(__name__)
CORS(app)

memory_users = []
memory_orders = []
memory_dogs = []
order_id = 0


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!!'


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
        new_user = User(
            body["name"],
            body["surname"],
            body["email"],
            body["password"]
        )
        memory_users.append(new_user.to_json())
        return {"Usuario": new_user.to_json(), "mensaje": "Usuario creado exitosamente", "status": "ok"}

    if is_get:
        return jsonify(memory_users)


@app.route('/api/v1/perros', methods=["GET", "POST", "POST"])
def Dogs():
    added = flask.request.method == 'POST'
    is_get = flask.request.method == 'GET'
    is_delete = flask.request.method == 'DELETE'

    if added:
        body = flask.request.json
        new_dog = Dog(
            body["name"],
            body["raza"],
            body["edad"],
            body["lugar"]
        )
        memory_dogs.append(new_dog.to_json())
        return {"Perro": new_dog.to_json(), "mensaje": "Masota agregada exitosamente", "status": "ok"}

    if is_get:
        return jsonify(memory_dogs)

    if is_delete:
        return "no se como es esto"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)