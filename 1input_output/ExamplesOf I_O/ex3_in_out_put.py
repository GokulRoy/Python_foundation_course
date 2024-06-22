# example3
# input: 10 20 30
# output: "sum:60"

# taking multiple numbers as str 
a = input()
# x,y,z = input().split(" ") also cane be written
# we give numbers in str then we split them using split("") keyword
x,y,z = a.split(" ")

# now we add them by converting them from str to int
sum = int(x) + int(y) + int(z)

# now we print sum by the following given output
print("sum:",sum,sep="")