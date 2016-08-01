

def a(n):
    rest = 1
    l = []
    div = []
    while(True):
        l.append(rest)
        rest = rest * 10
        k = rest/n
        div.append(k)
        rest = rest % n

        if(rest in l):
            return len(div[l.index(rest):])
        if(rest == 0):
            return 0
#
m = 0
out = 0
for i in range(1,1001):
    k = a(i)
    if (k>m):
        m = k
        out = i
print m,out

