# create the parent class
class Parent:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def myFun(self):
        print("hello!,",self.fname,self.lname)

# creating child class
class child(Parent):
    pass
# assigning values to  child class and printing them
x = Parent("Gokul","Roy")
x.myFun()
print(x.fname)
print(x.lname)

