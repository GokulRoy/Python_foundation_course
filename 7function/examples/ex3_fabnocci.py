
# series that has value greater than 100 stop there
def fab(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(n):
        c = a + b
        a = b
        b = c
        if c <= 100:
            print(c)
        else:
            print(f"from here the series value {c} will be grater than 100")
            break

fab(11)

