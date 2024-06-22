


from functools import reduce
# we need to import reduce from functools

def add_all(a,b):
    return a+b

num = [1,2,3,4,5,6,7,8,9,10]
print(num)
evens = list(filter(lambda x : x%2==0,num))
print(evens)
dobules = list(map(lambda n : n*2, evens))
print(dobules)
sum = reduce(add_all,dobules)
# using lambda -- sum = reduce(lambda a,b : a+b ,dobles)
print(sum)
