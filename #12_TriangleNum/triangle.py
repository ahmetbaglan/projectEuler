import time
def m(n):
    k = n
    d ={}
    index = 1
    max = 2
    while k>=2:
        index+=1
        if(k % index == 0):
            if(index in d.keys()):
                d[index]+=1
            else:
                d[index] = 1
            if(index>max):
                max = index
            k = k/index
            index = 1
    return d

def numDiv(d):
    divisor = 1
    for i in d:
        divisor *= (d[i]+1)
    return divisor


def bul(k):
    a = 0
    n = 1
    while k>a:
        sayi = n * (n+1) / 2
        d = m(sayi)
        a = numDiv(d)
        n = n+1
    print d
    return sayi


start = time.clock()
print bul(500)
print "time elapsed : ", time.clock()-start 