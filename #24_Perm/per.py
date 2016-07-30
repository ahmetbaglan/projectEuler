from eulerLib import *


def getNthPerm(l,n):
    a = len(l)
    b = l[:]
    out =()
    if(n <= 1):
        return tuple(l)
    for i in range(a-1,-1,-1):
        if(n>fact(i)):
            f = n/fact(i)
            n = n%fact(i)
            if(n == 0):
                f = f-1
                n=fact(i)
            k = (b[f],)
            b.remove(b[f])
            return k + getNthPerm(b,n)
        else:
            f = 0
            k = (b[f],)
            b.remove(b[f])

            return k + getNthPerm(b,n)



print getNthPerm([0,1,3],4)