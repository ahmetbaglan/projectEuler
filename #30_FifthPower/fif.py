from eulerLib import *
import time

def getSumOfNthPowerOfDigits(s,n):
    a = str(s)
    mysum = 0
    for k in a:
        k = int(k)
        mysum += power(k,n)
        if(mysum>s):
            return mysum
    return mysum

def findTheLogicalTreshold(n):

    for i in range(1000):
        k = (i * (10**n))/9**n
        if(k>(n+1)):
            return (i-1)*(10**n)
    return None



def f(n):
    s = 0
    threshold = findTheLogicalTreshold(n)
    if(threshold == None):
        print "threshold error"
        return None

    for i in range(10,threshold):
        if(getSumOfNthPowerOfDigits(i,n) == i):
            s+=i
            print i

    return s

start = time.clock()
print f(4)
print "time elapsed : ", time.clock()-start
