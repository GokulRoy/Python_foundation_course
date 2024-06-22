# creating class for 1st class = car
class Car:
    def __init__(self,barnd,model):
        self.brand = barnd
        self.model = model
    def move(self):
        print("Move!")
# creating class for 2nd class = boat
class Boat:
    def __init__(self,barnd,model):
        self.brand = barnd
        self.model = model
    def move(self):
        print("Sail!")
# creating class for 3rd class = plane
class Plane:
    def __init__(self,barnd,model):
        self.brand = barnd
        self.model = model
    def move(self):
        print("Fly!")
# assigning values in the object
car1 = Car("Ford",2019)
boat1 = Boat("ABC",2022)
plane1 = Plane("Indigo",2015)
# now by using for loop the values of object in the class are assigned
for x in (car1, boat1, plane1):
    # calling funtion
    x.move()