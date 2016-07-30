def mult(a,b):
    m = str(a)
    now = 0
    l = []
    eldevar = 0
    for i in range(b-1):

        for k in range(len(m)-1,-1,-1):
            now = int(m[k]) * a + eldevar
            eldevar = now/10
            l.append(now%10)
            if(k == 0 and eldevar != 0):
                l.append(eldevar)
                eldevar = 0
        m = l[::-1]
        l = []
        print
    print m
    sum = 0
    for l in m:
        sum+=l

    return sum

print mult(11,3)


