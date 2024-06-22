def abc():
    x = 100
    def cvd():
        nonlocal x
        x = 300
    cvd()
    return x
print(abc())