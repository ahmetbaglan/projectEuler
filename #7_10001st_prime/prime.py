def isPrime(a,l):
    for i in l:
        if( a%i == 0):
            return False
    return True

def getNthPrime(n):
    primes = [2]
    index = 3
    while(len(primes)<n):
        if(isPrime(index,primes)):
            primes.append(index)
        index+=2
    print len(primes)
    return primes[-1]

print getNthPrime(10001)
