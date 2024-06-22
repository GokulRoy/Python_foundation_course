num = [1,2,3,4,5,6,7,8,9]
# in buit fun in python "filter" and lambda
evens = list(filter(lambda n : n%2 == 0,num))
# maps used to perform funtion or method
double = list(map(lambda n : n*2,evens))
print(evens)
print(double)