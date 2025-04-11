class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"

# Create objects of each vehicle type
car = Car()
plane = Plane()
boat = Boat()

# Call move() for each vehicle
print(car.move())
print(plane.move())
print(boat.move())
