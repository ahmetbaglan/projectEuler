
def factor(n):
    tot = 1
    for i in range(1,n+1):
        tot *=i
    return tot

def rout(h,w):
    return factor(h+w)/(factor(h)*factor(w))

print rout(20,20)