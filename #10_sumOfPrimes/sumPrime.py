import math
def isPrime(a,l):

    index = 0
    for i in l:
        if( a%i == 0):
            return False
        if(i>math.sqrt(a)):
            break
    return True

def sumPrimes(n):
    primes = [2]
    for index in range(3,n,2):
        if(isPrime(index,primes)):
            primes.append(index)

    return sum(primes)

print sumPrimes(2*(10**6))
