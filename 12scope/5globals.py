a = 5
print("out fun",a)
print(id(a))
def som():
    a = 9
    x = globals()['a']
    print("in fun",a)
    print(id(x))
    globals()['a'] = 15
som()
print("out fun",a)
    