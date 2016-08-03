from eulerLib import  *

m = 0
ma = 0
mb = 0

for a in range(-1000,1001):
    for b in range(-1000,1001):
        n = 0
        while(True):
            k = n**2 + a * n + b
            if(k<0 or not is_prime(k)):
                if(n>m):
                    m = n
                    ma = a
                    mb = b
                break
            n+=1
    print a

print ma*mb
