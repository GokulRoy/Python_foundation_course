pos = 1


def bsearch(lst,n):
    l = 0
    u = len(lst)-1
    m = l+u//2

    for x in lst:
        if x == n:
            globals()['pos'] = lst.index(x)
            return True
        else:
            if lst[m]<n:
                l = m+1
            else:
                u = m-1
    return False

lst = [2,358,2455,54544,454,848,41,7,5,484844,454454,144758,1000,100,80]
lst.sort()
print(lst)
n=54544
if bsearch(lst,n):
    print(f"the element {n} is at position {pos}")
else:
    print("the element is not found in the list!")
    print("Enter the element which was in list")