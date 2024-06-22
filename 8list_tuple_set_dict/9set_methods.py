s1={1,2,3,4,5}
s2={4,5,6,7,8}
s={20,30,40,50,60}
# clear()
s2 = s2.clear()
print(s2)
# copy()
s2=s.copy()
print(s2)
# pop() removes 1 st value
s2.pop()
print(s2)
# update() it combines all values
s1.update(s2)
print(s1)
s2.update(s1)
print(s2)