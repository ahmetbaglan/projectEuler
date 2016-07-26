import  time
d = {}
def tilLOne(n):
    if(n in d):
        return d[n]
    elif(n == 1):
        return 1
    else:
        basla = n
        index = 1
        
        if(n%2 == 0):
            index = index + tilLOne(n/2)
        else:
            index = index +tilLOne(3*n + 1)
        d[basla] = index
        return  index
    return  None

def maxCol(k):
    m = 0
    mn = 0
    n = 0
    d = {}
    while(n<k):
        n += 1
        now= tilLOne(n)
        if now>m:
            m = now
            mn = n
    return m,mn


start = time.clock()
print maxCol(10**6)
print time.clock()-start
print tilLOne(100000)