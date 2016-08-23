import eulerLib as e

def check(n):
    a = str(n)
    top = 0
    for i in a:
        top += e.fact(int(i))
        if(top>n):
            return False

    if(top == n):
        return True
    return False


out = []
for i in range(1,10**6):
    if(check(i)):
        out.append(i)


k = 0
for i in out:
    k+=i

print k