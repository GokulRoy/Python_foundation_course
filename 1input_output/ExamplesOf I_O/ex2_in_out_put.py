# example2
# input: 5
# output: "You entered:5"
num = int(input("enter value: "))
print("You entered:",num)
print("You entered:",num,sep="")
# print("You entered:"+num)== we cant use + to concatenate int values.
# an only concatenate str (not "int") to str
