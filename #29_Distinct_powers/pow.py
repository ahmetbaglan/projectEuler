from eulerLib import *



def m(a,b):
    l = []
    for i in range(a,b+1):
        for j in range(a,b+1):
            k = power(i,j,isStr=True)
            if(k not in l):
                l.append(k)

    return len(l)


print m(2,100)