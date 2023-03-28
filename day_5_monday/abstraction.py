# Abstraction is the process of hiding the implementation details of a class and exposing only the relevant information to the user

import abc

class Vehicle(abc.ABC):
    @abc.abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        print("Driving a car...")

class Truck(Vehicle):
    def drive(self):
        print("Driving a truck...")

class Bike(Vehicle):
    def drive(self):
        print("Riding a bike...")

# create instances of each class
car = Car()
truck = Truck()
bike = Bike()

# call the drive method on each instance
car.drive()  # Output: Driving a car...
truck.drive()  # Output: Driving a truck...
bike.drive()  # Output: Riding a bike...
