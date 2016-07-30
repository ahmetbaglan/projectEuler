
def pr(ar_list):
    if not ar_list:
        yield ()
    else:
        for a in ar_list[0]:
            for prod in pr(ar_list[1:]):
                yield (a,) + prod

def topla(lines):
    m = 0
    for i in lines:
        if(len(i)>m):
            m = len(i)
    for i in range(len(lines)):
        if(len(lines[i])< m):
            lines[i] = '0'*(m-len(lines[i]))+lines[i]

    l = []
    eldevar = 0
    for i in range(len(lines[0])-1,-1,-1):
        top = 0
        for k in lines:
            top += int(k[i])
            top += eldevar
            eldevar = 0
        if(top >= 10):
            eldevar = top / 10
        l.append(top % 10)

    if( eldevar > 0):
        for s in str(eldevar)[::-1]:
            l.append(s)

    l = l[::-1]
    return  l

def mult(a,b):
    """
    Classical multiplication
    """
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
    """
    Factorial
    """
    if(n == 0 or n == 1):
        return  1
    else:
        return mult(n,fact(n-1))

def carpanlaraAyir(n):
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

def getEvenDivisors(n):
    d= carpanlaraAyir(n)
    allList = []
    for i in d.keys():
        now = []
        for k in range(d[i]+1):
            now.append(i**k)
        allList.append(now)

    out = []
    f = list(pr(allList))

    for i in f:
        sum = 1
        for k in i:
            sum*=k
        out.append(sum)

    return out


def perm(l):
    l = sorted(l)
    b = l[:]
    out = []
    if(len(l) == 1):
        return  [(l[0],)]
    for i in l:
        b.remove(i)
        for k in perm(b):
            out.append((i,) + k)
        b = l[:]
    return out



