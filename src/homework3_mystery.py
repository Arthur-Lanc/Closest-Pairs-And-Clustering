import math

def mystery(a,l,r):
    if l > r:
        return -1
    m = int(math.floor((l+r)/2))
    if a[m] == m:
        return m
    else:
        if a[m] < m:
            return mystery(a,m+1,r)
        else:
            return mystery(a,l,m-1)

        
print mystery([i for i in range(0,7)],0,6)