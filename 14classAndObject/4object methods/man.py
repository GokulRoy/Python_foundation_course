# funtions that belong to object
# create class
class Man:
    # define init
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # now creat funtion to call new one by self
    def myFun(self):
        print("Hello!,",self.name)
# create object
p1 = Man("Jhon", 30)
# print the name and age
print(p1.name)
print(p1.age)
# calling def fun to print the myFun by assigning p1
p1.myFun()

# method
# modifing object parametrs
# modify
p1.age = 40
print(p1.age)
# delete 
