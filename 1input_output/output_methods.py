a = int(input("give a value: "))
b = int(input("give b value: "))

print(a,b)
# using sep the output statement
print(a,b,sep=",")
# using sep the output statement
print(a,b,a,b,sep=",",end=" end here.")

# formating out put using f-string
x,y=input("name and age:").split(",")
print(f"Name:{x},Age:{y} years")
