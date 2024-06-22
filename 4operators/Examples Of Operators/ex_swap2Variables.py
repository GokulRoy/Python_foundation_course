# swap the values of two variables without
# i: a = 10; b = 20
# o: a = 20; b = 10
a = int(input("a = "))
b = int(input("b = "))

# using a temporary variable
# temp = a
# a = b 
# b = temp
# print(f"a = {a}")
# print(f"b = {b}")

# without using a temporary variable
a += b        #a=a+b; a=10+20; a=30
b = a - b     #b=30-20; b=10
a = a - b     #a=30-10; a=20
print(f"a = {a}")
print(f"b = {b}")