class per:
    def __init__(self):
        self.name = "gokul"
        self.age = 22
    def update(self):
        self.age = 30
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False
c1 = per()
c1.age = 30
c2 = per()
if c1.compare(c2):
    print("they are same")
else:
    print("they are not same")
print(c1.name)
print(c1.age)