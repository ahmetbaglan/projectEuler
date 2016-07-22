def getFib(a,b):
    return a+b

def getEvenFibTotal(r):
    totalEven = 2
    a = 1
    b = 2
    print a
    print b
    for i in range(r-2):
        temp = getFib(a,b)
        a = b
        b = temp
        if(temp % 2 == 0):
            totalEven+=temp
        print temp
    print "And the toatal is", totalEven

getEvenFibTotal(10)