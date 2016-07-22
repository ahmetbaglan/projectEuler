def getFib(a,b):
    return a+b

def getEvenFibTotal(r):
    totalEven = 2
    a = 1
    b = 2
    while(b<r):
        temp = getFib(a,b)
        a = b
        b = temp
        if(temp % 2 == 0):
            if(b>r):
                break
            print temp
            totalEven+=temp
    print "And the toatal is", totalEven

getEvenFibTotal(4000000)
