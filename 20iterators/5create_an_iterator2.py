class numbers:
    def __init__(self):
        self.a = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
vals = numbers()
nums = iter(vals)
for i in nums:
    print(i)
