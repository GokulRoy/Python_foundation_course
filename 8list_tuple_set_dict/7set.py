# empty set
s_1 = {}
f = {'apple','bannana','cherry'}
# creating a set from list
l = [1,2,3,4,5]
print(l)
s_l = set(l)
print(s_l)

# method
# add() to add element
f.add('straberry')
print(f)
# remove() or discard()
s_l.remove(2)
s_l.discard(1)
print(s_l)
# frozen set
fr = frozenset(s_1)
print(fr)

# comprehension set
sq = {x**2 for x in range(0,6)}
print(sq)
