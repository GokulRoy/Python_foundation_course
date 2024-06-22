def div(a,b):
    print(a/b)
div(4,2)
div(2,4)

# here only by oder the output is coming


# now we add some logic
def div_1(a,b):
    if a < b:
        a,b = b,a
        print(a/b)
div_1(2,4)