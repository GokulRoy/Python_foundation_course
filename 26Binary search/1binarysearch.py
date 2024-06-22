pos = -1
def bsear(lst,n):
    L = 0
    U = len(lst)-1
    while L <= U:
        M = (L+U)//2
        if lst[M] == n:
            globals()['pos'] = M
            return True        
        else:
            if lst[M]<n:
                L = M+1
            else:
                U = M-1
    return False
lst = [5454,44,5545,14545,4545,411,45541,5,2,7,15845,48,8]
lst.sort()
print(lst)
# lst1 = nlst.sort()
# lst = list(lst1)
n = 5545
if bsear(lst,n):
    print(f"the value {n} found at position {pos+1}")
else:
    print("value not in list!, enter another number")