def pers(name, **data):
    print("name "+name)
    for i,j in data.items():
        print(i,j)
pers('gokul',age=22, city='tpty',moblno=1234567890)
