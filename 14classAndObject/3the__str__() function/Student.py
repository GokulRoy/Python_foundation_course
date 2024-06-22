# giving input
n = input("Enter name:")
    # x = input("Enter name:")
a = int(input("Enter age:"))
    # y = int(input("Enter age:"))
# create a class
class Student:
# now using def and __init__() crate 
# object properties
    #self is default and name age are variables
    def __init__(self, name, age): 
        # call the variables using default self and input variables
        self.n = name
        self.a = age
    # we use __str__() to print string represention
    # of the defined object in class and object
    def __str__(self):
        return f"{self.n}({self.a})"
# now create object p1 to insert values
p1 = Student(n, a)
# p1 = Person(x, y)
# now print the age and name using object and input vriables
print(p1.n)
print(p1.a)
# now we can print the fun in string format
print(p1)