# first we need to define by *
def sum(a, *b):
    # then we need to use for loop
    c = 0
    for i in b:
        c = c + i
    #now printing the sum  
    print(c)
# calling the fun by different numbers
sum(5,6,3,10,9,2,20)
