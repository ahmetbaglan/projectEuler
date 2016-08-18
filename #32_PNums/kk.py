import itertools

a = '--123456789'
a = list(a)
memory = []
def check(f):
    l = f.split('-')
    a = int(l[0])
    b =int(l[1])
    c= int(l[2])
    if(a in memory or b in memory or c in memory):
        return 0
    if(a*b==c):
        memory.append(c)
        return c
    elif(a*c==b):
        memory.append(b)
        return b
    elif(b*c ==a):
        memory.append(a)
        return a
    return 0

permlist= []
jok = itertools.permutations(a)
out = 0

for i in jok:
    c=''
    for k in i:
        c+=k
    if('--' not in c and c[-1] != '-' and c[0]!='-'):
        top = check(c)
        if(top>0):
            print top
        out+=top

print out

