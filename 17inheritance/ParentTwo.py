# using init()
# create the parent class and c
class ParentTwo:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def myFun(self):
        print("hello!,",self.fname,self.lname)

# creating child class
class child(ParentTwo):
    # adding init() by using  variables in the parent class
    def __init__(self, fname, lname):
        # calling init() parent class name and variables in the parent class
        ParentTwo.__init__(self, fname, lname)
# assigning values to  child class and printing them
x = child("Gokul","Roy")
x.myFun()
print(x.fname)
print(x.lname)

