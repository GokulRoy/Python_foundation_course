# tuple
x = ("apple","bannana","cherry")
# covert into list
y = list(x)
# now add to list
y[1]="kiwi"
# now change to tuple
x = tuple(y)
print(x)

# method 2
thistuple = ("apple", "banana", "cherry")
a = ("orange",)
thistuple += a

print(thistuple)