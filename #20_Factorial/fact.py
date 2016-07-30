def mult(a,b):
    m = str(a)
    now = 0
    l = []
    eldevar = 0

    for k in range(len(m)-1,-1,-1):
        now = int(m[k]) * b + eldevar
        eldevar = now/10
        l.append(now%10)
        if(k == 0 and eldevar != 0):
            l.append(eldevar)
            eldevar = 0
    m = l[::-1]

    out = ''
    for i in m:
        out += str(i)

    return  int(out)


def fact(n):
    if(n == 0 or n == 1):
        return  1
    else:
        return mult(n,fact(n-1))

def getsum(n):
    a = str(n)
    sum = 0
    for i in a:
        sum+= int(i)
    return sum


print getsum(fact(100))