
# =====================================
# FLEETEASE - VEHICLE CLASS
# =====================================

class Vehicle:

    def __init__(self, vehicle_id, name, price, fuel, seats, image):
        self.vehicle_id = vehicle_id
        self.name = name
        self.__price = price  # Encapsulation
        self.fuel = fuel
        self.seats = seats
        self.image = image

    @property
    def price(self):
        return self.__price

    def get_category(self):
        return "Vehicle"

    def to_dict(self):
        return {
            "id": self.vehicle_id,
            "name": self.name,
            "category": self.get_category(),
            "price": self.price,
            "fuel": self.fuel,
            "seats": self.seats,
            "image": self.image
        }


# =====================================
# CAR CLASS - INHERITANCE
# =====================================

class Car(Vehicle):

    def get_category(self):
        return "Car"


# =====================================
# BIKE CLASS - INHERITANCE
# =====================================

class Bike(Vehicle):

    def get_category(self):
        return "Bike"
