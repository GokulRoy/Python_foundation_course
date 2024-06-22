# example4
# input: "Jhon",25
# output: "Name:jhon,Age:25"
a = input()
x,y=a.split(",")
y=int(y)
print("Name:",x,",Age:",y,sep="")