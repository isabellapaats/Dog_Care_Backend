import flask
from flask import Flask, jsonify, request, json
from flask_cors import CORS
from models import Order, User, Dog

app = Flask(__name__)
CORS(app)

memory_users = []
memory_orders = []
memory_dogs = []
order_id = 0
user_id = 0


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!!'


@app.route('/api/v1/orders', methods=["GET", "POST"])
def Orders():

    is_get_all = flask.request.method == 'GET'
    is_create = flask.request.method == 'POST'

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
        user_id_gen = generate_user_id()
        body = flask.request.json
        new_user = User(
            user_id_gen,
            body["name"],
            body["surname"],
            body["email"],
            body["password"]
        )

        if loop(new_user.email):
            return {"mensaje": "Ya hay una cuenta asociada a este email"}
        else:
            memory_users.append(new_user.to_json())
            return {"Usuario": new_user.to_json(), "mensaje": "Usuario creado exitosamente", "status": "ok"}

    if is_get:
        return jsonify(memory_users)



def loop(x):
    b = ""
    if (len(memory_users) != 0):
        for a in memory_users:
            if (a["email"] == x):
                b = True
        return b
    else:
        return False


def generate_user_id():
    user_id.__add__(1)
    return str((len(memory_users) + 1)).rjust(10, "0")


@app.route('/api/v1/registros/<id_usuario>', methods=["DELETE", "GET", "PUT"])
def delete(id_usuario):

    if flask.request.method == 'DELETE':
        for user in memory_users:
            if user["user_id"] == id_usuario:
                memory_users.remove(user)
                return jsonify({"Usuario": user, "mensaje": "Usuario eliminado exitosamente", "status": "ok"})

    if flask.request.method == 'PUT':
        body = flask.request.json

        for user in memory_users:
            if user["user_id"] == id_usuario:
                if user["password"] != body["newpassword"]:
                    user["password"] = body["newpassword"]
                    return jsonify({"mensaje": "Contrase??a actualizada exitosamente", "status": "ok"})
                else:
                    user["password"] = user["password"]
                    return jsonify({"mensaje": "Ingrese una contrase??a distinta a la anterior", "status": "ok"})


@app.route('/api/v1/perros', methods=["GET", "POST"])
def Dogs():
    added = flask.request.method == 'POST'
    is_get = flask.request.method == 'GET'

    if added:
        body = flask.request.json
        new_dog = Dog(
            body["name"],
            body["edad"],
            body["tel"],
            body["lugar"],
            body["img"]
        )
        memory_dogs.append(new_dog.to_json())
        return {"Perro": new_dog.to_json(), "mensaje": "Masota agregada exitosamente", "status": "ok"}

    if is_get:
        return jsonify(memory_dogs)


@app.route('/api/v1/perro', methods=["GET"])
def buscarPerro():
    is_get = flask.request.method == 'GET'

    if is_get:
        nombre = request.args.get('name')
        perros_found = []
        for dog in memory_dogs:
            if dog['name'] == nombre:
                perros_found.append(dog)

        return jsonify(perros_found)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)