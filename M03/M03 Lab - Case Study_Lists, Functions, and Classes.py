# M03 Lab - Case Study: Lists, Functions, and Classes
# David N Drummond
# SDEV220 Lab assignment

"""Write a Python app that has the following classes:
A super class called Vehicle, which contains an attribute for vehicle type, such as car, truck, plane, boat, or a broomstick.
A class called Automobile which will inherit the attributes from Vehicle and also contain the following attributes:
    year
    make
    model
    doors (2 or 4)
    roof (solid or sun roof).
Write an app that will accept user input for a car. The app will store "car" into the vehicle type in your Vehicle super class. 
The app will then ask the user for the year, make, model, doors, and type of roof and store thdata in the attributes above.
The app will then output the data in an easy-to-read and understandable format, such as this:
  Vehicle type: car
  Year: 2022
  Make: Toyota
  Model: Corolla
  Number of doors: 4
  Type of roof: sun roof"""

class Vehicle():
    def __init__(self,vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    #Initialize the class and variables
    def __init__(self):
        vehicle_type = "car"
        year = input("What year was your car made?")
        make = input("What is the make of the vehicle?")
        model = input("What is the model of the vehicle?")
        doors = input("Does the vehicle have 2 or 4 doors?\n Enter '2' or '4'.")
        roof = input("What type of roof does your vehicle have?")

        self.vehicle_type = vehicle_type
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    
    def report(self):
        print("\n Vehicle Report")
        print("Vehicle Type: " + self.vehicle_type)
        print("Year: " + self.year)
        print("Make: " + self.make)
        print("Model: " + self.model)
        print("Number of doors: " + self.doors)
        print("Roof: " + self.roof)
    

    

car = Automobile()
car.report()

    