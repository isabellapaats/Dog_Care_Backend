class Order:
    def __init__(self, order_id, name, surname, phoneNumber, location, postalCode, email, pedidos):
        self.order_id = order_id
        self.name = name
        self.surname = surname
        self.phoneNumber = phoneNumber
        self.location = location
        self.postalCode = postalCode
        self.email = email
        self.pedidos = pedidos

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


class ChangeUser:
    def __init__(self, newpassword):
        self.newpassword = newpassword

    def to_json(self):
        return self.__dict__


class Dog:
    def __init__(self, name, raza, edad, lugar, img):
        self.name = name
        self.raza = raza
        self.edad = edad
        self.lugar = lugar
        self.img = img

    def to_json(self):
        return self.__dict__