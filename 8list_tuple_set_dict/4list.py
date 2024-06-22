# creating list
# empty list
E_l = []
# number list
Num_l = [1,2,3,4]
# name list
word_l = ["apple", "bannana", "cherry"]
# mixed list
m_l = [1,"hi", 3.25, True]
print(type(Num_l))
print(type(m_l))
# list comprehension
l = [x**2 for x in range(0,5)]
print(l)

n = int(input("enter size of list:"))
List1 = list(map(float,input("enter the elements in list seperated by space:").split()))
List2 = list(map(int,input("enter the elements in list seperated by comma:").split(",")))
print(List1)
print(List2)