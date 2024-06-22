# adding and methods
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
#   here we add the year in parameters
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    # here we called the parameter
    self.graduationyear = year
# here we created the function
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
# here we call the fun
x.welcome()
