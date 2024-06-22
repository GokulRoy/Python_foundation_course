def ev_od(lst):
    e = 0
    o = 0
    for i in lst:
        if i%2==0:
            e += 1
        else:
            o += 1
    return e,o
lst1=input("enter by coma:").split(",")
lst = [int(x) for x in lst1]
print(lst)
e,o = ev_od(lst)
print("no of even numbers are",e)
print("no of odd numbers are",o)

