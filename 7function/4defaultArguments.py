# giving default value in def fun itself
def great_person(name,greetings="Hello"):
    return greetings + ", " + name + "!"
per1 = great_person("Gokul")
per2 = great_person("Chenchu")
print(per1)
print(per2)