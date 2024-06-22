# method 1
# input can be placed before def fun
a = int(input())
b = int(input())
def add_2num(a,b):
    print(a+b)
add_2num(a,b)

# method 2
def add_2num(c,d):
    print(c+d)
# input can also 10
# be placed after def fun
c = int(input())
d = int(input())
add_2num(c,d)