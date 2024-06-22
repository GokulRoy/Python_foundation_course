# giving input
n = input("Enter name:")
    # x = input("Enter name:")
a = int(input("Enter age:"))
    # y = int(input("Enter age:"))
# create a class
class person:
# now using def and __init__() crate 
# object properties
    #self is default and name age are variables
    def __init__(self,name,age): 
        # call the variables using default self and input variables
        self.n = name
        self.a = age
# now create object p1 to insert values
p1 = person(n, a)
# p1 = Person(x, y)
# now print the age and name using object and input vriables
print(p1.n)
print(p1.a)
# if we only asks to print object by calling
# object name it will print is location
print(p1)