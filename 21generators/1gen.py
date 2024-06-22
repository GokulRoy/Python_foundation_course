# generators give iterators
def topten():
    # yield is akeyword that iterate the given num
    yield 1
    yield 2
    yield 3
    yield 4

values = topten()
# we can print using this or this
# print(values.__next__())
# print(values.__next__())
# print(values.__next__())

# or this
for i in values:
    print(i)
