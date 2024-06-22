# using keyword global
x = 300
def a_b():
    global x
    x = 200
    print(x*2)
a_b()
print(x)