# crating the parent class vehicle
class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Move!")
# now craeting child class Car and inheriting 
# whole properties and funtions
class Car(Vehicle):
    pass #adding pass key word to print without error
# now craeting child class boat and inheriting 
# whole properties of class vehicle and only init()
class Boat(Vehicle):
    # now creating move() funtion as sail!
    def move(self):
        print("Sail!")
# now craeting child class boat and inheriting 
# whole properties of class vehicle and only init()
class Plane(Vehicle):
    # now creating move() funtion as sail!
    def move(self):
        print("fly!")
# now crating object for the class 
car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object
for x in (car1,boat1,plane1):
    print(x.brand)
    print(x.model)
    x.move()