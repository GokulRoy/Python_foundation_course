# printing numbers using iter and def
# creating a class
class Mynum:
    # crating def __iter__() to assign value to self
    def __iter__(self):
        self.a = 1
        return self
    # crating __next__() to loop the values of next number
    def __next__(self):
        x = self.a
        self.a += 1
        return x
# assign value of class mynum() to myclass
myClass = Mynum()
# iterating my class and storing as myiter object
myiter = iter(myClass)
# printing
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))