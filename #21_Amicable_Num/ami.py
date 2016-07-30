from eulerLib import *

def d(n):
    divisors = getEvenDivisors(n)
    sum = 0
    for i in divisors:
        sum+=i
    sum -= n
    return sum
l = []
for i in range(2,10000):

    a = d(i)
    if(d(a) == i):
        if(a<10000 and a!=i):
            l.append(a)



print sum(l)

