def is_even(n):
    return n%2 == 0

num = [1,2,3,4,5,6,7,8,9]
# in buit fun in python "filter"
# used to get only wanted things 
evens = list(filter(is_even,num))

print(evens)


# method 2
# num = [1,2,3,4,5,6,7,8,9]
# # in buit fun in python "filter" and lambda
# evens = list(filter(lambda n : n%2 == 0,num))
# print(evens)
