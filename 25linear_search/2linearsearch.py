# linear search using for
pos = -1
def sear(lst,n):
    for x in lst:
        if x == n:
            globals()['pos'] = lst.index(x)
            return True
    return False
lst = [5,3,9,7,1,6,4]
n = 7
if sear(lst,n):
    print("Element fount at",pos+1)
else:
    print("Element not found! enter other n")