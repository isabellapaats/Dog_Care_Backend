class Order:
    def __init__(self, order_id, customer_name, customer_surname, phone_number, address, postalCode, email, pedido):
        self.order_id = order_id
        self.customer_name = customer_name
        self.customer_surname = customer_surname
        self.phone_number = phone_number
        self.address = address
        self.postalCode = postalCode
        self.email = email
        self.pedido = pedido

    def to_json(self):
        return self.__dict__


class User:
    def __init__(self, user_id, name, surname,email, password):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password

    def to_json(self):
        return self.__dict__


class changeUser:
    def __init__(self, newpassword):
        self.newpassword = newpassword

    def to_json(self):
        return self.__dict__

class Dog:
    def __init__(self, name, raza, edad, lugar):
        self.name = name
        self.raza = raza
        self.edad = edad
        self.lugar = lugar

    def to_json(self):
        return self.__dict__