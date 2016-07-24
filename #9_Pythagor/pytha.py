def isPyt(a,b,c):

    if(a<0 or b<0 or c<0):
        return False

    return a**2 == c**2 + b**2

def f(n):
    for a in range(n/3+1,n):
        for b in range(max(n - (2*a - 1),0),a):
            c  = n - a - b
            if(isPyt(a,b,c)):
                return a*b*c




print f(1000)