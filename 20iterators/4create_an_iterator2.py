class numbers:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        x = self.num
        self.num += 1
        return x
values = numbers()
myit = iter(values)
print(myit.__next__())
print(myit.__next__())
print(myit.__next__())
