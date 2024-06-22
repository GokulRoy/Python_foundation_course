# zip used to connect various data
names = ('gokul','jhon','mike')
comps = ('dell','apple','ms')
zipped1 = zip(names,comps)
zipped2 = list(zip(names,comps))
zipped3 = set(zip(names,comps))
zipped4 = dict(zip(names,comps))
print(zipped1)
print(zipped2)
print(zipped3)
print(zipped4)
for (a,b) in zipped1:
    print(a,b)