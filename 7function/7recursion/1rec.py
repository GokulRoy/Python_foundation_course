# recursion calling a fun in a fun itself
def greet():
    print("hello")
    # here we called the fun in fun itself
    greet()
greet()
# only printing limit is 1000