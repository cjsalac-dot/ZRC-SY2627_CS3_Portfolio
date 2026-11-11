#1.A. Duck typing is a programming concept where an object's suitability is determined by the presence of methods andc properties rather than its explicit class inheritance.
#1.B The car class needed to have a method with the exact same name like make_sound() as the Dog and Cat classes.

class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")

def start_trip(vehicle):
    vehicle.move()

# Create one object of each class
car_obj = Car()
boat_obj = Boat()
drone_obj = Drone()

# Call start_trip() for each object
start_trip(car_obj)
start_trip(boat_obj)
start_trip(drone_obj)