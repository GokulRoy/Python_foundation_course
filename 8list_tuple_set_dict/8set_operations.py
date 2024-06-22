# operations of set
s1={1,2,3,4,5}
s2={4,5,6,7,8}
# union (adds both and remove common elemants)
su = s1.union(s2)
print(su)
# intersection (prints only common values)
si = s1.intersection(s2)
print(si)
# difference (prints difference of each side)
sd1 = s1.difference(s2) 
sd2 = s2.difference(s1)
print(sd1)
print(sd2)
# symetric difference (total differnce)
ssd = s1.symmetric_difference(s2)
print(ssd)

