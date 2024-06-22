# here x is outside it is called global
x=300
def mfun():
    # the x value available for whole fun
    print(x)
mfun()
print(x)