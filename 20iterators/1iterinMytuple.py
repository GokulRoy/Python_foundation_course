# creating a tuple
myTuple = ("apple", "banana", "cherry")
# now iterating using iter
myit = iter(myTuple)
# now printing using next for iterated my tuple = myit
print(next(myit))
print(next(myit))
print(next(myit))


# another
Tuple = ("apple", "banana", "cherry")
# now iterating using iter
it = iter(Tuple)
# now printing using next for iterated my tuple = myit
print(it.__next__())
print(it.__next__())
print(it.__next__())

