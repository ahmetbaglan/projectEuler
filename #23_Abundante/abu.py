from eulerLib import *

def ab(n):
    l  = []
    for i in range(2,n):
        if(sum(getEvenDivisors(i)[:-1])>i):
            l.append(i)



    return l

l = ab(30000)

def check(l,n):
    for i in l:
        if( (n-i) in l):
            return True
        if(i>n):
            break
    return False


check(l,24)
sum = 0
for i in range(30000,-1,-1):
    if(not check(l,i)):
        sum += i
print sum

